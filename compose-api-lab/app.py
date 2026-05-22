import os
import psycopg2
from psycopg2.extras import RealDictCursor
from flask import Flask, request, jsonify

app = Flask(__name__)

# ⚙️ Функція підключення до бази даних (Бере дані з файлу .env)
def get_db():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],         # Назва сервісу ('db')
        port=os.environ.get("DB_PORT", "5432"),
        dbname=os.environ["DB_NAME"],       # 'taskdb'
        user=os.environ["DB_USER"],         # 'apiuser'
        password=os.environ["DB_PASS"],     # 'apipass123'
        cursor_factory=RealDictCursor       # Повертає результати як зручні словники
    )

# 🛠️ Ініціалізація бази даних при запуску коду
def init_db():
    conn = get_db()
    cur = conn.cursor()
    # Цей блок дублює створення таблиці про всяк випадок
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title VARCHAR(200) NOT NULL,
            description TEXT DEFAULT '',
            done BOOLEAN DEFAULT FALSE,
            created_at TIMESTAMP DEFAULT NOW()
        )
    """)
    conn.commit()
    cur.close()
    conn.close()

# 📥 1. GET /tasks — Отримати список усіх задач
@app.route("/tasks", methods=["GET"])
def get_tasks():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks ORDER BY created_at DESC")
    tasks = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify(tasks)

# 📤 2. POST /tasks — Створити нову задачу
@app.route("/tasks", methods=["POST"])
def create_task():
    data = request.get_json()
    if not data or not data.get("title"):
        return jsonify({"error": "title is required"}), 400

    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO tasks (title, description) VALUES (%s, %s) RETURNING *",
        (data["title"], data.get("description", ""))
    )
    task = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(task), 201

# 🔍 3. GET /tasks/<id> — Знайти одну задачу за її номером (ID)
@app.route("/tasks/<int:task_id>", methods=["GET"])
def get_task(task_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM tasks WHERE id = %s", (task_id,))
    task = cur.fetchone()
    cur.close()
    conn.close()
    if not task:
        return jsonify({"error": "not found"}), 404
    return jsonify(task)

# ✏️ 4. PUT /tasks/<id> — Відредагувати задачу або позначити як виконану
@app.route("/tasks/<int:task_id>", methods=["PUT"])
def update_task(task_id):
    data = request.get_json()
    conn = get_db()
    cur = conn.cursor()
    cur.execute(
        """UPDATE tasks
           SET title = COALESCE(%s, title),
               description = COALESCE(%s, description),
               done = COALESCE(%s, done)
           WHERE id = %s RETURNING *""",
        (data.get("title"), data.get("description"), data.get("done"), task_id)
    )
    task = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if not task:
        return jsonify({"error": "not found"}), 404
    return jsonify(task)

# ❌ 5. DELETE /tasks/<id> — Видалити задачу з бази
@app.route("/tasks/<int:task_id>", methods=["DELETE"])
def delete_task(task_id):
    conn = get_db()
    cur = conn.cursor()
    cur.execute("DELETE FROM tasks WHERE id = %s RETURNING id", (task_id,))
    deleted = cur.fetchone()
    conn.commit()
    cur.close()
    conn.close()
    if not deleted:
        return jsonify({"error": "not found"}), 404
    return jsonify({"deleted": task_id})

# 🩺 6. GET /health — Перевірка зв'язку між сервером та базою даних
@app.route("/health", methods=["GET"])
def health():
    try:
        conn = get_db()
        cur = conn.cursor()
        cur.execute("SELECT 1")
        cur.close()
        conn.close()
        return jsonify({"status": "ok", "db": "connected"})
    except Exception as e:
        return jsonify({"status": "error", "db": str(e)}), 500

# 🏁 Запуск додатка
if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5000, debug=True)