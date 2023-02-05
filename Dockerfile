FROM python:3.11.1-slim

ENV POETRY_VIRTUALENVS_CREATE=false
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --no-cache-dir poetry
COPY poetry.lock pyproject.toml /app/
RUN poetry install --only main --no-root

COPY manage.py /app/
COPY api /app/api
COPY lpdalle /app/lpdalle
COPY users /app/users

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]