from models.jump import Jump
from models.response import Response

import json
import requests

from flask import Flask, request

app = Flask(__name__)

@app.route('/jump', methods=['GET', 'POST'])
def jump():
    if request.method == 'GET':
        print("Received GET /jump")
        res = Response("/ - Greetings from Python!", 200)
        print(res.to_string())
        return res.to_json()
    
    if request.method == 'POST':
        str_data = json.dumps(request.get_json())
        print("Received POST /jump with 1 JUMP.jumps - " + str_data)
    
        jump = json.loads(str_data, object_hook=lambda d: Jump(**d))
        res = Response("/ - Farewell from Python! Bad request by default", 400)

        if len(jump.jumps) == 1:
            r = requests.get(jump.jumps[0] + jump.last_path)
            r_data = json.dumps(r.json())
            res = json.loads(r_data, object_hook=lambda d: Response(**d))

        if len(jump.jumps) == 2:
            res = Response("/ - Greetings from Python! 2 ", 200)

        return res.to_json()

    glob_res = Response("/ - Farewell from Python! - Bad Request", 400)
    return glob_res.to_json()
