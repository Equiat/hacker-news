# Hacker News Clone





## Technologies 

The following technologies were used in this project:

- [HTML](https://html.com/)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)


## Requirements

Before starting, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

## Activate the virtual environment

    . venv/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Create an admin user profile

    python manage.py createsuperuser

## Collect Static files

    python manage.py collectstatic

## Start server

    python manage.py runserver
