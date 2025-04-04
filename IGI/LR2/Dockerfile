FROM python:3.9-slim

WORKDIR /app

# Копируем ВСЕ файлы
COPY . .

# Устанавливаем пакет в режиме разработки
RUN pip install -e .

CMD ["python", "main.py"]