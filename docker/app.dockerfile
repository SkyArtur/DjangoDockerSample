FROM python:3.11-alpine
LABEL maintainer="SkyArtur"
WORKDIR /var/www
COPY . .
RUN apk update &&  \
    apk add zlib-dev jpeg-dev gcc musl-dev python3-dev postgresql-dev &&  \
    pip install -r requirements.txt &&  \
    python manage.py collectstatic --noinput
ENTRYPOINT gunicorn --bind 0.0.0.0:8000 appSetup.wsgi
EXPOSE 8000