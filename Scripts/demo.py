# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-05-05 15:07
# @File    : demo.py
# @Software: PyCharm
# import json
# import requests
# import operator
#
#
# def send_request(data):
#     with open('expect.txt', 'a+', encoding="utf-8") as f:
#         f.write(data['TestId'])
#         f.write('-')
#         f.write(data['Title'])
#         f.write('\n')
#
#     response = requests.post(data['Url'], data=data['body'])
#     res = response.json()
#     # return res
#     with open('result.txt', 'a+', encoding='utf-8') as rst:
#         rst.write('返回数据')
#         rst.write('|')
#         rst.write(str(res))
#
#         # 写测试结果
#         try:
#             if operator.eq(res, data['Result']):
#                 rst.write('pass')
#             else:
#                 rst.write('fail')
#         except Exception:
#             rst.write('no except result')
#         rst.write('\n')
#
#
# with open("./data/data.json", "r", encoding="utf-8") as f:
#     res = json.load(f)
# send_request(res)


import requests
import unittest
import json


# class TestLogin(unittest.TestCase):
#
#     def setUp(self):
#         self.session = requests.session()
#
#     def test_login(self):
#         url = "http://127.0.0.1:8000/login/"
#         data = {
#             "username": "admin",
#             "password": "123456"
#         }
#         response = self.session.post(url=url, json=data)
#         result = response.json()
#         print(result)
#         self.assertEqual("200", result['error_code'])
#         self.assertEqual("登陆成功", result['msg'])
#
#     def tearDown(self):
#         self.session.close()

sign_in_url = "http://127.0.0.1:8000/sign_in/"
login_url = "http://127.0.0.1:8000/login/"
change_password_url = "http://127.0.0.1:8000/change_password/"
login_data = {
    "username": "admin",
    "password": "1234567"
}
change_password_data = {
    'username': 'admin',
    'userToken': 'KurHOEvrqK2MmDy81WqakmibQnL06Q',
    'new_password': '123456'
}
response = requests.post(url=login_url, data=login_data)
# result = json.dumps(response.json(), ensure_ascii=False)
result = response.json()
print(result)
