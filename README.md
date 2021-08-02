# Hacker News Clone

This is a Django web application that retrieves data from Hacker News API and makes it easier to navigate the news items. It provides search and filter functionality and also enables clients, through three API endpoints, to create news items, modify and delete only the items they created and provide read-only access to news items generated from Hacker News API server. 


## Technologies 

The following technologies were used in this project:

- [HTML](https://html.com/)
- [CSS](https://developer.mozilla.org/en-US/docs/Learn/CSS/First_steps)
- [Python](https://www.python.org/)
- [Django](https://www.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Hacker News API](https://hackernews.api-docs.io/v0/overview/introduction)
- [SQLite3](https://www.sqlite.org/index.html)


## Requirements

Before starting, you need to have [Git](https://git-scm.com) and [Python](https://www.python.org/) installed.

Kindly ensure that you are in the root directory before running the following commands.

## Create a virtual environment

    python3 -m venv env

## Activate the virtual environment

    . env/bin/activate

## Install dependencies

    pip install -r requirements.txt

## Make migrations

    python manage.py makemigrations

## Migrate apps and database

    python manage.py migrate

## Collect Static files

    python manage.py collectstatic

## Run Tests

    python manage.py test

## Fetch data from Hacker News API

    python manage.py shell < hn_api.py

## Start server
    Open another terminal window, activate the virtual environment and run the following command:

    . env/bin/activate && python manage.py runserver


# Endpoints

The endpoints, expected payloads, and responses are described below.


## Get all news items 

### Request

`GET api/v1/news/`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/api/v1/news/

### Response

    {
        "message": "success",
        "data": {
            "news": [
                {
                    "id": "b9bb893c-92f3-4ce6-acb6-ce28a357b3ab",
                    "title": "How to walk across a parking lot (2011)",
                    "author": "baobaba",
                    "type": "story",
                    "url": "https://www.raptitude.com/2011/09/how-to-walk-across-a-parking-lot/",
                    "text": "",
                    "score": 2,
                    "is_from_api": true
                },
                {
                    "id": "bdd5a967-be3c-403c-9022-3fcf3a48d318",
                    "title": "Ad Ode to Temporal",
                    "author": "debuggerpk",
                    "type": "story",
                    "url": "https://debugger.pk/ode-to-temporal/",
                    "text": "",
                    "score": 1,
                    "is_from_api": true
                }
            ]
        },
        "errors": null
    }

## Create a news item

### Request

`POST api/v1/add-news`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/api/v1/add-news

### Payload

    {
        "title": <String>,
        "author": <String>,
        "type": <String>
        "text": <String>
        "score": <Integer>
    }

### Response

    {
        "message": "success",
        "data": {
            "news": {
                "id": <UUID>,
                "title": <String>,
                "author": <String>,
                "type": <String>
                "url": <String>,
                "text": <String>
                "score": <Integer>,
                "is_from_api": <Boolean>
            }
        },
        "errors": null
    }


## Get a specific news item by its ID

### Request

`GET api/v1/news/<id>`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/api/v1/news/<id>

### Response

    {
        "message": "success",
        "data": {
            "news": {
                "id": <UUID>,
                "title": <String>,
                "author": <String>,
                "type": <String>
                "url": <String>,
                "text": <String>
                "score": <Integer>,
                "is_from_api": <Boolean>
            }
        },
        "errors": null
    }


## Update a news item

### Request

`PUT api/v1/news/<id>`

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/api/v1/news/<id>

### Payload

    {
        "title": <String>,
        "author": <String>,
        "type": <String>
        "text": <String>
        "score": <Integer>
    }

### Response

    {
        "message": "success",
        "data": {
            "news": {
                "id": <UUID>,
                "title": <String>,
                "author": <String>,
                "type": <String>
                "url": <String>,
                "text": <String>
                "score": <Integer>,
                "is_from_api": <Boolean>
            }
        },
        "errors": null
    }


## Delete a news item

### Request

`DELETE api/v1/news/<id>` 

    curl -i -H 'Accept: application/json' http://127.0.0.1:8000/api/vi/news/<id>

### Response

    {
        "message": "success",
        "data": {
            "news": {}
        },
        "errors": null
    }
