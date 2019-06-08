import random
import json
import string
import requests
import sys
from Scripts.Util.logger import *
from Scripts.conf.config import Conf


class Util(object):
    logger = Log()

    @staticmethod
    def send_request(url_name, data, method="GET"):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
        }
        response = None
        if method == "GET":
            response = requests.get(Conf.urlMap[url_name], headers=headers)
        elif method == "POST":
            response = requests.post(Conf.urlMap[url_name], data=data, headers=headers)
        try:
            res = response.json()
            return res
        except Exception:
            return response.text

    @staticmethod
    def get_json(file_name):
        res_list = []
        with open("./data/" + file_name + ".json", "r", encoding="utf-8") as f:
            res = json.load(f)

        for i in res.values():
            demo_list = list()
            for a in i.items():
                demo_list.append(a)
            res_list.append(demo_list)
        return res_list

    @staticmethod
    def random_str(length):
        random_str_list = [random.choice(string.digits + string.ascii_letters) for _ in range(length)]
        random_str = ''.join(random_str_list)
        return random_str

    def userToken(self):
        url = Conf.msg['login']
        data = self.get_json("login")[0]
        # print(data)
        r = requests.post(url, data)
        res = r.json()
        return res['userToken']

    @staticmethod
    def write_static_files(msg, lines):
        str_msg = str(msg)
        static_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        res_path = os.path.join(static_path, "static/")
        if not os.path.exists(res_path):
            os.mkdir(res_path)
        function_name = str(sys._getframe().f_back.f_code.co_name)
        file_name = str(os.path.join(res_path, function_name)) + "-assert_file.txt"
        file_name_except = str(os.path.join(res_path, function_name)) + ".txt"
        if os.path.exists(file_name_except):
            with open(file_name_except, "r", encoding="utf-8") as f:
                except_file = f.read()
            if except_file == "":
                with open(file_name_except, "a", encoding="utf-8") as f:
                    f.write(str_msg + "\n")
            else:
                count = 0
                for _, _ in enumerate(open(file_name_except, 'r', encoding="utf-8")):
                    count += 1
                if count < lines:
                    with open(file_name_except, "a", encoding="utf-8") as f:
                        f.write(str_msg + "\n")
        else:
            os.system(r'touch %s' % file_name_except)
            count = 0
            for _, _ in enumerate(open(file_name_except, 'r', encoding="utf-8")):
                count += 1
            if count < lines:
                with open(file_name_except, "a", encoding="utf-8") as f:
                    f.write(str_msg + "\n")

        if os.path.exists(file_name):
            count = 0
            for _, _ in enumerate(open(file_name, 'r', encoding="utf-8")):
                count += 1
            if count >= lines:
                os.remove(file_name)
        else:
            os.system(r'touch %s' % file_name)
        os.system(r'touch %s' % file_name)
        count = 0
        for _, _ in enumerate(open(file_name, 'r', encoding="utf-8")):
            count += 1
        if count < lines:
            with open(file_name, 'a', encoding="utf-8") as f:
                f.write(str_msg + "\n")

    @staticmethod
    def __assert_equal(msg, except_msg):
        if type(msg) != type(except_msg):
            raise TypeError("类型不同")

        try:
            assert msg == except_msg
        except AssertionError:
            Util.logger.error(str(msg) + "!=" + str(except_msg))
            raise AssertionError

    @staticmethod
    def assert_equal(func_name, skip=None):
        static_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
        os.path.join(static_path, "static/")
        # function_name = str(sys._getframe().f_back.f_code.co_name)
        res_path = os.path.join(static_path, "static/")
        except_file_name = str(os.path.join(res_path, func_name)) + ".txt"
        res_except_file_name = str(os.path.join(res_path, func_name)) + "-assert_file.txt"
        # print("进行比较：{} 和 {}".format(except_file_name, res_except_file_name))
        with open(res_except_file_name, "r", encoding="utf-8") as f:
            res_msg = f.read()
        with open(except_file_name, "r", encoding="utf-8") as f:
            res = f.read()
        if res == "" or res_msg == "":
            return
        Util.__assert_equal(res_msg, res)


if __name__ == '__main__':
    # print(Util.get_json("login"))
    # print(Util().userToken())
    # Util.write_static_files("1231234")
    Util.assert_equal('test_login', skip='userToken')
