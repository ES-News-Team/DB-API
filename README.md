# DB-API
O objetivo desse projeto e oferecer uma persistência de dados para os serviços de notícias.

# Tecnologia
Python 3.6 ou superior. Link para donwload e instalação: https://www.python.org/downloads/

Link para instalar pip: https://pip.pypa.io/en/stable/installation/

**Instalar Docker: https://docs.docker.com/engine/install/**  

**Instalar Docker Compose: https://docs.docker.com/compose/install/**

# Integrantes
Daniel de Souza Lima Junior  
Natalia Bíscaro  
Guilherme Garcia  

# Montando um Ambiente
Esses procedimentos devem ser feitos na raiz do projeto, e são exemplos em ambiente `Unix/Mac`.
1. Como criar [virtual environments](https://docs.python.org/3/library/venv.html)  
    ```
    python3 -m pip install virtualenv
    ```
2. Criando um ambiente virtual   
    ```
    python3 -m venv venv && source venv/bin/activate
    ```
3. Instalando dependências
    ```
    pip install -r requirements.txt
    ```
    As dependências usanda nesse projeto são:
    ```
    # Dependências do Flask-RESTful
    aniso8601==9.0.1
    click==8.1.2
    Flask==2.1.1
    Flask-RESTful==0.3.9
    itsdangerous==2.1.2
    Jinja2==3.1.1
    MarkupSafe==2.1.1
    pytz==2022.1
    six==1.16.0
    Werkzeug==2.1.1

    # Dependências do Flask
    click==8.1.2
    Flask==2.1.1
    itsdangerous==2.1.2
    Jinja2==3.1.1
    MarkupSafe==2.1.1
    Werkzeug==2.1.1

    # Dependências do SQLAlchemy
    greenlet==1.1.2
    SQLAlchemy==1.4.35

    # Dependências do Flask-Bcrypt
    bcrypt==3.2.0
    cffi==1.15.0
    click==8.1.2
    Flask==2.1.1
    Flask-Bcrypt==1.0.1
    itsdangerous==2.1.2
    Jinja2==3.1.1
    MarkupSafe==2.1.1
    pycparser==2.21
    six==1.16.0
    Werkzeug==2.1.1

    # mariadb
    mariadb==1.0.11

    # dependências do gunicorn
    gunicorn==20.1.0
    ```

# Desenvolvimento
```
docker-compose -f db-api-service/develop.compose up --build
```

# Produção
```
docker-compose -f db-api-service/production.compose up --build
```
