# DockerDjangoSample

Teste de deploy de uma aplicação django em containers Docker.

### Tecnologia envolvidas

- [ Docker Desktop &copy; ](https://www.docker.com/)
- [ Django &reg; ](https://www.djangoproject.com/)
- [ Python &trade; ](https://www.python.org/)
- [ Yalm &trade; ](https://yaml.org/)

Execute o comando em um terminal aberto na pasta raiz do projeto.

````shell
docker-compose up -d
````

A seguir execute as migrações no container 'app'.

````shell
docker exec app python manage.py makemigrations
docker exec app python manage.py migrate
docker exec -it app python manage.py createsuperuser
````

Acesse seu navegador em http://localhost:8080.

![Captura de tela 2023-08-31 230116.png](images%2FCaptura%20de%20tela%202023-08-31%20230116.png)
