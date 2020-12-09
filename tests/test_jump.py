from flask import Flask, request
from jump import app

import json

def test_get_home():
    with app.test_client() as c:
        rv = c.get('/')
        json_data = json.loads(rv.data)
        response = {'code': 200, 'message': '/ - Greetings from Python!'}
        assert json_data == response

def test_get_jump():
    with app.test_client() as c:
        rv = c.get('/jump')
        json_data = json.loads(rv.data)
        response = {'code': 200, 'message': '/jump - Greetings from Python!'}
        assert json_data == response
