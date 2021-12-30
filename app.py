from models.jump import Jump
from models.jump_response import JumpResponse

import json
import requests
import copy

from flask import Flask, request, Response

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

    res = JumpResponse("/ - Greetings from Python!", 200)
    print(res.to_string())
    return res.to_json()

@app.route('/jump', methods=['GET', 'POST'])
def jump():
    if request.method == 'GET':
        print("------------------")
        print("Received GET /jump")
        headers = request.headers
        print(headers)

        react_modifier = resolve_header(headers, 'React-Modifier')
        x_request_id = resolve_header(headers, 'X-Request-Id')
        x_b3_traceid = resolve_header(headers, 'X-B3-Traceid')
        x_b3_spanid = resolve_header(headers, 'X-B3-Spanid')
        x_b3_parentspanid = resolve_header(headers, 'X-B3-Parentspanid')
        x_b3_sampled = resolve_header(headers, 'X-B3-Sampled')
        x_b3_flags = resolve_header(headers, 'X-B3-Flags')
        x_ot_span_context = resolve_header(headers, 'X-Ot-Span-Context')

        res = JumpResponse("/jump - Greetings from Python!", 200)
        print(res.to_string())

        resp = Response(res.to_json())
        resp.headers['React-Modifier'] = resolve_header(headers, 'React-Modifier')
        resp.headers['X-Request-Id'] = resolve_header(headers, 'X-Request-Id')
        resp.headers['X-B3-Traceid'] = resolve_header(headers, 'X-B3-Traceid')
        resp.headers['X-B3-Spanid'] = resolve_header(headers, 'X-B3-Spanid')
        resp.headers['X-B3-Parentspanid'] = resolve_header(headers, 'X-B3-Parentspanid')
        resp.headers['X-B3-Sampled'] = resolve_header(headers, 'X-B3-Sampled')
        resp.headers['X-B3-Flags'] = resolve_header(headers, 'X-B3-Flags')
        resp.headers['X-Ot-Span-Context'] = resolve_header(headers, 'X-Ot-Span-Context')

        return resp
    
    if request.method == 'POST':
        str_data = json.dumps(request.get_json())
        print("------------------")
        print("Received POST /jump with multi JUMP.jumps - " + str_data)
        headers = request.headers
        print(headers)
    
        jump = json.loads(str_data, object_hook=lambda d: Jump(**d))
        res = JumpResponse("/jump - Farewell from Python! Bad request by default", 400)

        react_modifier = resolve_header(headers, 'React-Modifier')
        x_request_id = resolve_header(headers, 'X-Request-Id')
        x_b3_traceid = resolve_header(headers, 'X-B3-Traceid')
        x_b3_spanid = resolve_header(headers, 'X-B3-Spanid')
        x_b3_parentspanid = resolve_header(headers, 'X-B3-Parentspanid')
        x_b3_sampled = resolve_header(headers, 'X-B3-Sampled')
        x_b3_flags = resolve_header(headers, 'X-B3-Flags')
        x_ot_span_context = resolve_header(headers, 'X-Ot-Span-Context')
        
        headers_req = {'Content-Type': 'application/json; utf-8', 
            'Accept': 'application/json', 
            'React-Modifier': react_modifier,
            'X-Request-Id': x_request_id,
            'X-B3-Traceid': x_b3_traceid,
            'X-B3-Spanid': x_b3_spanid,
            'X-B3-parentspPnid': x_b3_parentspanid,
            'X-B3-Sampled': x_b3_sampled,
            'X-B3-Flags': x_b3_flags,
            'X-Ot-Span-Context': x_ot_span_context
        }

        print(headers_req)

        if len(jump.jumps) == 1:
            print("Received POST /jump with multi JUMP.jumps - " + str_data)
            url = jump.jumps[0] + jump.last_path
            try:
                r = requests.get(url, headers=headers_req)
                r_data = json.dumps(r.json())
                res = json.loads(r_data, object_hook=lambda d: JumpResponse(**d))
            except: 
                res = JumpResponse("/jump - Farewell from Python! Error Jumping", 400)
                
        if len(jump.jumps) > 1:
            print("Received POST /jump with multi JUMP.jumps - " + str_data)
            url = jump.jumps[0] + jump.jump_path
            try:
                req_jump = copy.copy(jump.jumps)
                req_jump = req_jump[1:]
                jump.jumps = req_jump
                p = requests.post(url, headers=headers_req, data=jump.to_json())
                p_data = json.dumps(p.json())
            except:
                res = json.loads(p_data, object_hook=lambda d: JumpResponse(**d))

        resp = Response(res.to_json())
        resp.headers['React-Modifier'] = resolve_header(headers, 'React-Modifier')
        resp.headers['X-Request-Id'] = resolve_header(headers, 'X-Request-Id')
        resp.headers['X-B3-Traceid'] = resolve_header(headers, 'X-B3-Traceid')
        resp.headers['X-B3-Spanid'] = resolve_header(headers, 'X-B3-Spanid')
        resp.headers['X-B3-Parentspanid'] = resolve_header(headers, 'X-B3-Parentspanid')
        resp.headers['X-B3-Sampled'] = resolve_header(headers, 'X-B3-Sampled')
        resp.headers['X-B3-Flags'] = resolve_header(headers, 'X-B3-Flags')
        resp.headers['X-Ot-Span-Context'] = resolve_header(headers, 'X-Ot-Span-Context')

        return resp

    glob_res = JumpResponse("/jump - Farewell from Python! - Bad Request", 400)
    return glob_res.to_json()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)