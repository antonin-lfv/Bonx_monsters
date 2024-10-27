# syntax=docker/dockerfile:1

ARG PYTHON_VERSION=3.11.1
FROM python:${PYTHON_VERSION}-slim AS base

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

# Copier le code source dans le conteneur
COPY . .

# Installer les dépendances
RUN pip install --no-cache-dir -r requirements.txt

# Créer un utilisateur non privilégié
ARG UID=10001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "/nonexistent" \
    --shell "/sbin/nologin" \
    --no-create-home \
    --uid "${UID}" \
    appuser

# Changer les permissions des fichiers pour appuser
RUN chown -R appuser /app

# Passer à l'utilisateur non privilégié
USER appuser

EXPOSE 8000

CMD ["python", "app.py"]