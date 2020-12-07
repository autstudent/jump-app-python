from typing import Tuple

import json

class Jump:
    def __init__(self, message: str, jump_path: int, last_path: int, jumps: Tuple[str, ...]):
        self.message = message
        self.jump_path = jump_path
        self.last_path = last_path
        self.jumps = jumps

    def to_string(self):
        string = "Jump[message: " + self.message + " ,jump_path: " + self.jump_path + " ,last_path: "  + self.last_path + " ,jumps: " + str(self.jumps) + "]"
        return string

    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)

            