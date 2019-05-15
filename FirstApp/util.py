import json
import random
import string


class Util:

    @staticmethod
    def json_response(msg):
        response = json.dumps(msg, ensure_ascii=False)
        return response
