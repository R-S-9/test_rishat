# Instructions for the developer
## Installation and launch

1. Clone a repository from Github:
```
git@github.com:R-S-9/test_project.git
```
2. Create a virtual environment:
```
python -m venv venv
```
3. Activate the environment:
```
source venv/bin/activate
```
4. In the file .evn fill in the required data.

## Installing dependencies
1. Install requirements
```
pip install -r requirements.txt
```
2. Create and apply migrations to the database:
```
python manage.py makemigrations
python manage.py migrate
```

## Launch surrounded by the developer
Create a database in PostgreSQL and point to `settings.py`. Example:
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'testproject',
        'USER': 'postgres',
        'PASSWORD': 'password',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}
```
Start the server:
```
cd src
python manage.py runserver --insecure
```
## Launching the Docker
```
docker build .            
docker-compose build 
docker-compose up         
```
