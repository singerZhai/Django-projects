import json
import random
import string

main_url = "127.0.0.1:8000"


class Util:

    # 获取 token
    def userToken(self, length=30):
        random_str_list = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
        userToken = ''.join(random_str_list)
        return userToken

    def json_response(self, msg):
        response = json.dumps(msg, ensure_ascii=False)
        return response
