import random
import json
import string
import requests
import configparser

path = "../conf/"
main_url = "http://0.0.0.0:8000"


class Conf(object):

    __main_url = "http://127.0.0.1:8000"
    msg = {
        'login': __main_url + '/login/',
        'sign_in': __main_url + '/sign_in/',
        'change_password': __main_url + '/change_password/',
    }


class Base(configparser.ConfigParser):

    def __as_dict(self):
        res = dict(self._sections)
        for i in res:
            res[i] = dict(res[i])
        return res

    # 读取配置文件中的 case 如果有"*"或者"?"的话 自动生成动态 case
    def read_ini_case(self, file_name):
        self.read(path + file_name + ".ini", encoding="utf-8")
        res = self.__as_dict()
        res_dict = {}
        flag = 0
        for i in res.values():
            i.pop('desc')
            res_dict[str(flag)] = i
            flag += 1

        flag = 0
        res_case = {}
        for i in res_dict.values():
            i_json = json.dumps(i)
            if "*" in i:
                res = i['*'].split(',')
                i.pop('*')
                for key in res:
                    a = json.loads(i_json)
                    a.pop(key)
                    res_case[str(flag)] = a
                    flag += 1
            elif "?" in i:
                res = i['?'].split(',')
                i.pop('?')
                for key in res:
                    a = json.loads(i_json)
                    a[key] = ''
                    res_case[str(flag)] = a
                    flag += 1
            else:
                res_case[str(flag)] = i
                flag += 1
        for i in res_case.values():
            if "*" in i:
                i.pop("*")
            elif "?" in i:
                i.pop("?")
        return res_case

    @staticmethod
    def random_str(length):
        random_str_list = [random.choice(string.digits + string.ascii_letters) for i in range(length)]
        random_str = ''.join(random_str_list)
        return random_str

    def userToken(self):
        url = Conf.msg['login']
        data = self.read_ini_case('login')['0']
        r = requests.post(url, data)
        res = r.json()
        return res['userToken']


if __name__ == '__main__':
    conf = Base()
    print(conf.read_ini_case("login"))
    # print(Base().userToken())
