# Практичні роботи з Docker & Kubernetes

**Виконала:** Єва  
**Група:** ІПЗ-31  

У цьому репозиторії зібрано всі 6 виконаних практичних робіт з контейнеризації та оркестрації додатка.

---

## 📂 Структура репозиторію

* 📁 **[task-1](./task-1)** — Контейнеризація базового додатка на Python/Flask (створення `Dockerfile`).
* 📁 **[task-2](./task-2)** — Робота з `Docker Volumes` (збереження даних у СУБД PostgreSQL).
* 📁 **[task-3](./task-3)** — Зв'язування додатка та бази даних через `Docker Compose` (`healthcheck`, `.env`).
* 📁 **[task-4](./task-4)** — Full-Stack додаток (Task Tracker) з Frontend на Nginx, Backend на Flask та СУБД PostgreSQL (налаштовано `CORS`).
* 📁 **[task-5](./task-5)** — Перший `Deployment` у Kubernetes (масштабування реплік, оновлення версії додатка через `Rollout`).
* 📁 **[task-6](./task-6)** — Налаштування `Kubernetes Service` (ClusterIP) для балансування навантаження та впровадження `readinessProbe` (/health).

---

## 🚀 Як запустити фінальний проєкт (Task 4):
1. Перейти в папку завдання: `cd task-4`
2. Запустити Docker Compose: `docker compose up -d --build`
3. Відкрити веб-інтерфейс у браузері: `http://localhost:8080`