# Python Demo App

## Introduction

Python Demo App is one of a set of microservices, named Jumps, developed to generate a microservice communication test tool in order to support multi hands-on and webinars around microservices in Kubernetes.

## Quick Start Flask

```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install Flask
...
```

## Quick Start Python Demo App

```
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=jump.py
$ flask run
```

## Python Demo App Test

Python Demo App included a set of test in order to check all features.

```
$ <WIP>
```

## Test Python Demo App API Locally

- GET method to reach /jump

```
$ curl localhost:5000/jump
{
    "code": 200,
    "message": "/ - Greetings from Python!"
}
```

- POST method with JUMP Object in the body to make simple jump through Python Demo

```
$ curl -XPOST -H "Content-type: application/json" -v -d '{
    "message": "Hello",
    "last_path": "/jump",
    "jump_path": "/jump",
    "jumps": [
        "http://localhost:5000"
    ]
}' 'localhost:5000/jump'
{
    "code": 200,
    "message": "/ - Greetings from Python!"
}
```

- POST method with JUMP Object in the body to make multi jumps through Python Demo

```
$ curl -XPOST -H "Content-type: application/json" -v -d '{
    "message": "Hello",
    "last_path": "/jump",
    "jump_path": "/jump",
    "jumps": [
        "http://localhost:5000",
        "http://localhost:5000"
    ]
}' 'localhost:5000/jump'
{
    "code": 200,
    "message": "/ - Greetings from Python!"
}
```
