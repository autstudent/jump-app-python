# Python Demo App

## Introduction

Python Demo App is one of a set of microservices, named Jumps, developed to generate a microservice communication test tool in order to support multi hands-on and webinars around microservices in Kubernetes.

## Quick Start Python Demo App

```bash
$ python3 -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ export FLASK_APP=app.py
$ flask run
```

## Python Demo App Test

Python Demo App included a set of test in order to check all features.

```bash
$ pytest -v
====================================== test session starts =======================================
platform darwin -- Python 3.8.2, pytest-6.1.2, py-1.9.0, pluggy-0.13.1 -- .../python-demo/venv/bin/python3
cachedir: .pytest_cache
rootdir: .../python-demo
collected 2 items

tests/test_app.py::test_get_home PASSED                                                    [ 50%]
tests/test_app.py::test_get_jump PASSED                                                    [100%]

======================================= 2 passed in 0.16s ========================================
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
