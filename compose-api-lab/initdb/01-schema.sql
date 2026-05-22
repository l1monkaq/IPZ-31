CREATE TABLE IF NOT EXISTS tasks (
    id SERIAL PRIMARY KEY,          -- Автоматичний номер задачі (1, 2, 3...)
    title VARCHAR(200) NOT NULL,    -- Назва задачі (обов'язково)
    description TEXT DEFAULT '',    -- Опис задачі
    done BOOLEAN DEFAULT FALSE,     -- Статус (виконано/ні)
    created_at TIMESTAMP DEFAULT NOW() -- Час створення
);