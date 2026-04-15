FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends     build-essential     libpq-dev     curl     netcat-openbsd     && rm -rf /var/lib/apt/lists/*

COPY requirements /tmp/requirements
RUN pip install --no-cache-dir -r /tmp/requirements/production.txt

COPY ./src /app
COPY ./docker/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
