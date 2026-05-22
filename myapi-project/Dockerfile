# Використовуємо офіційний легкий образ Python
FROM python:3.10-slim

# Робоча директорія всередині контейнера
WORKDIR /app

# Копіюємо файл із залежностями та встановлюємо їх
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Копіюємо весь код додатка в контейнер
COPY . .

# Відкриваємо порт 5000 для зовнішнього світу
EXPOSE 5000

# Команда для запуску додатка
CMD ["python", "app.py"]