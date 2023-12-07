                   Инструкция по запуску

# Создаем базу данных
1)psql
2)create database {название бд}

# Создаем и активируем виртуальное окружение 
1)python3 -m venv venv
2). venv/bin/activate

# Скачиваем зависмости 
1) pip install -r requirements.txt

# Get - запрос
http://localhost:8000/

# Post - запрос
http://localhost:8000/create_book/

# Put - запрос
http://localhost:8000/update_item/1/ (надо передать данные для обновления)

# Delete - запрос
http://localhost:8000/delete_book/6/

