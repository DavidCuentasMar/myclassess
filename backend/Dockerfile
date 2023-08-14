FROM python:3.11.4-alpine3.18

WORKDIR /app
COPY . /app

RUN set -e; \
    apk add --no-cache --virtual .build-deps \
    gcc \
    libc-dev \
    linux-headers \
    ; \
    pip install -r requirements.txt; \
    apk del .build-deps;

ENTRYPOINT ["uwsgi", "app.ini"]