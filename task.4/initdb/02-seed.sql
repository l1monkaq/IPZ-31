-- Наповнення таблиці початковими завданнями з лабораторної роботи
INSERT INTO tasks (title, description, done) VALUES
    ('Встановити Docker', 'Завантажити та встановити Docker Desktop на локальну машину', TRUE),
    ('Вивчити Dockerfile', 'Розібрати базові інструкції: FROM, COPY, RUN, CMD, EXPOSE', TRUE),
    ('Вивчити Docker Compose', 'Зрозуміти роботу директив: services, volumes, networks, depends_on', FALSE),
    ('Створити REST API', 'Розгорнути зв''язку Flask + PostgreSQL в ізольованих контейнерах', FALSE);