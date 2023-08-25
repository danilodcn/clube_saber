FROM python:3.10-alpine3.18

WORKDIR /app

RUN apk update --no-cache && apk add --no-cache build-base postgresql-dev musl-dev

RUN pip install --no-cache -U pip poetry psycopg2-binary

COPY pyproject.toml poetry.lock /app/

RUN poetry config virtualenvs.create false && \
    poetry install --only main --no-root --no-cache
COPY . .

RUN mkdir -p static

CMD [ "sh", "entrypoint.sh" ]