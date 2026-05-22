import os
from flask import Flask, jsonify

app = Flask(__name__)

# Версія додатку для відстеження оновлень (Rollout)
VERSION = "1.0.1"

@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "status": "ok",
        "message": "Привіт з Kubernetes кластера! 👋",
        "version": VERSION
    })

@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200

if __name__ == "__main__":
    print(f"Starting python-backend v{VERSION}...")
    # Сервер слухає порт 5000
    app.run(host="0.0.0.0", port=5000)