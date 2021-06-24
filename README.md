# Django Job Application

It's a raw application for managing jobs which should be executed
in the given Microservice-structure of `JangasNLPFunPlace`.

Only django admin is used for simplifying that process.


## Setup & Requirements

There are two possible ways for setting up the application:
1. Docker
2. Python


### Requirements (Python)

- Python 3.7 or higher
- Postgres Database
- poetry or pip


### Setup (Python)

1. Install requirements `poetry install` or
    `pip install -r requirements.txt`
2. Update env file: `cp app/.env.example app/.env`. You need to
    update postgres credentials, kafka credentials and superuser info
3. Migrate the database `python app/manage.py migrate`
4. Create superuser `python app/manage.py initialsuperuser`
5. Runserver `python app/manage.py runserver`
6. Open http://localhost:8000/
7. Have fun

### Setup (Docker)
1. Update env file: `cp app/.env.example app/.env`. You need to
    update superuser information
2. start the docker composition: `docker-compose up -d`
3. Open http://localhost:8000/
4. Have fun
