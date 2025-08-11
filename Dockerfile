FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY config ./config
COPY querymaze ./querymaze
COPY manage.py .
COPY requirements.txt .
COPY wait-for-it.sh .

RUN chmod +x wait-for-it.sh
RUN pip install --upgrade pip && pip install -r requirements.txt

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]