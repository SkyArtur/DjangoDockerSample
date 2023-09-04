FROM postgres:13.1-alpine
LABEL maintainer="SkyArtur"
ENV POSTGRES_DB=app_django_database
ENV POSTGRES_USER=app_user
ENV POSTGRES_PASSWORD=app_pass
EXPOSE 5432
