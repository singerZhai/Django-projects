import json
import random
import string


class Util:

    # 获取 token
    @staticmethod
    def userToken(length=30):
        random_str_list = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
        userToken = ''.join(random_str_list)
        return userToken

    @staticmethod
    def json_response(msg):
        response = json.dumps(msg, ensure_ascii=False)
        return response
