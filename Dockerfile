# Используем официальный образ Python (версия 3.10, можно изменить под свои нужды)
FROM python:3.10-slim

# Отключаем создание .pyc файлов и буферизацию вывода
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Задаём рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл с зависимостями и устанавливаем их
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Копируем исходный код проекта в контейнер
COPY . /app/

# Копируем entrypoint скрипт и делаем его исполняемым
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Запускаем скрипт при старте контейнера
CMD ["/entrypoint.sh"]