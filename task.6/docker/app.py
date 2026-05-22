import os
import socket
from flask import Flask, jsonify

app = Flask(__name__)

VERSION = "2.0.0"
POD_NAME = socket.gethostname()  # Kubernetes автоматично ставить сюди унікальне ім'я пода

@app.route("/", methods=["GET"])
def hello():
    # Повертаємо ім'я пода, щоб у терміналі бачити, як балансується трафік
    message = f"Hello from pod {POD_NAME} (version {VERSION})\n"
    print(f"[{POD_NAME}] Handled request — 200 OK")
    return message

@app.route("/health", methods=["GET"])
def health():
    # Ендпоінт для перевірки готовності (readinessProbe)
    return "OK\n", 200

if __name__ == "__main__":
    print(f"Starting python-backend {VERSION} on pod {POD_NAME}...")
    app.run(host="0.0.0.0", port=5000)