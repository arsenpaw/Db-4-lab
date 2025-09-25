# syntax=docker/dockerfile:1
FROM python:3.11-slim

WORKDIR /app
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# ✅ Deps required to build mysqlclient wheels
RUN apt-get update && apt-get install -y --no-install-recommends \
    pkg-config \
    default-libmysqlclient-dev \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Flask dev server (embedded)
ENV FLASK_APP=app.py FLASK_RUN_HOST=0.0.0.0 FLASK_RUN_PORT=5000
EXPOSE 5000
CMD ["flask", "run"]
