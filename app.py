from models.jump import Jump
from models.response import Response

import json
import requests

from flask import Flask, request

app = Flask(__name__)

def resolve_header(headers, key):
    try:
        return headers[key]
    except:
        return ""

@app.route('/', methods=['GET'])
def home():
    print("Received GET /")
    headers = request.headers
    print(headers)
    
    res = Response("/ - Greetings from Python!", 200)
    print(res.to_string())
    return res.to_json()

@app.route('/jump', methods=['GET', 'POST'])
def jump():
    if request.method == 'GET':
        print("Received GET /jump")
        headers = request.headers
        print(headers)

        res = Response("/jump - Greetings from Python!", 200)
        print(res.to_string())
        return res.to_json()
    
    if request.method == 'POST':
        str_data = json.dumps(request.get_json())
        print("Received POST /jump with 1 JUMP.jumps - " + str_data)
        headers = request.headers
        print(headers)
    
        jump = json.loads(str_data, object_hook=lambda d: Jump(**d))
        res = Response("/jump - Farewell from Python! Bad request by default", 400)

        react_modifier = resolve_header(headers, 'React-Modifier')
        x_request_id = resolve_header(headers, 'x-request-id')
        
        headers_req = {'Content-Type': 'application/json; utf-8', 
            'Accept': 'application/json', 
            'React-Modifier': react_modifier,
            'x-request-id': x_request_id}

        if len(jump.jumps) == 1:
            url = jump.jumps[0] + jump.last_path
            r = requests.get(url , headers=headers_req)
            r_data = json.dumps(r.json())
            res = json.loads(r_data, object_hook=lambda d: Response(**d))

        if len(jump.jumps) > 1:
            new_jump = jump
            new_jump.jumps = new_jump.jumps[1:]
            url = jump.jumps[0] + jump.jump_path
            try:
                p = requests.post(url , headers=headers_req, data=new_jump.to_json())
                p_data = json.dumps(p.json())
                res = json.loads(p_data, object_hook=lambda d: Response(**d))
            except: 
                res = Response("/jump - Farewell from Python! Error Jumping", 400)

        return res.to_json()

    glob_res = Response("/jump - Farewell from Python! - Bad Request", 400)
    return glob_res.to_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)