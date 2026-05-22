@echo off
:: 1. Створення іменованого тому для збереження даних бази
docker volume create pg_data

:: 2. Запуск контейнера PostgreSQL з підключенням створеного тому
docker run -d --name task2-postgres -e POSTGRES_PASSWORD=mysecretpassword -v pg_data:/var/lib/postgresql/data -p 5432:5432 postgres:16-alpine

:: 3. Перевірка статусу запущеного контейнера
docker ps

:: 4. Перевірка списку створених томів у системі
docker volume ls