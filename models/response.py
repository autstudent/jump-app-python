import json

class Response:
    def __init__(self, message: str, code: int):
        self.message = message
        self.code = code

    def to_string(self):
        string = "Response[code: " + str(self.code) + " ,message: " + self.message + "]"
        return string

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)