from fastapi import FastAPI
import psycopg2
import os

app = FastAPI()

@app.get("/")
def home():
    return {"message": "FastAPI працює!"}

@app.get("/db")
def check_db():
    try:
        conn = psycopg2.connect(os.getenv("DATABASE_URL"))
        conn.close()
        return {"db": "Підключення успішне!"}
    except Exception as e:
        return {"db": "Помилка", "error": str(e)}
