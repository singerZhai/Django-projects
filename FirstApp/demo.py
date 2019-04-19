# import requests
#
#
# data = {
#     'username': 'admin',
#     'password': 'admin123'
# }
#
# r = requests.post("http://127.0.0.1:8000/login/", data=data)
# print(r.headers)
# print(r.text)


# demo = '"BxGAbKiDVNi5MWlaOgzIASgsBeuTHg"'
# res = demo.replace('"', '')
# print(res)


# demo = [{'name': 'xiaoming', 'age': 18},
#         {'name': 'xiaohong', 'age': 20},
#         {'name': 'zhangsan', 'age': 30},
#         {'name': 'lisi', 'age': 40}]
#
# a = "-"
#
# for i in demo:
#     print(i['name'].ljust(10), end='')
#     print(a.center(5), end='')
#     print(str(i['age']).rjust(1) + "岁")


# class Demo(object):
# #
# #     name = "admin"
# #
# #     def doing(self):
# #         print("Hello World")
# #
# #
# # doing = getattr(Demo, 'doing')
# # # isinstance()
# # print(doing)
# # doing(object)


# class Demo(object):
#
#     @staticmethod
#     def doing(**kwargs):
#         print(kwargs)
#
#
# demo = getattr('./', 'Demo')
# # demo(username='admin', password='123456')
# demo.doing()


# class Manager:
#     role = "管理员"
#
#     def createClass(self):
#         print("create class")
#
#     @staticmethod
#     def createStu():
#         print("createStu")
# from FirstApp.demo1 import *


# f = getattr("Manager", "createClass")
# f(object)

# f = getattr(Manager, "createClass")
# f(object)
#
# role = getattr(Manager, "createStu")
# role()
#
# # 对象获取类属性
# role = getattr(Manager, "role")
# print(role)


# def run():
#     inp = input("请输入您想访问页面的url： ").strip()
#     print(inp)
#     modules, func = inp.split("/")
#     print(modules + ">>>>>>" + func)
#     obj = __import__(modules)
#     if hasattr(obj, func):
#         func = getattr(obj, func)
#         func()
#     else:
#         print("404")
#
#
# if __name__ == '__main__':
#     run()

# demo = "demo1/login"
# print(demo)
# demo1, demo2 = demo.split('/')
# print(demo1)
# print(demo2)


# demo = __import__('demo1')
# obj = getattr(demo, 'Demo')
#
# obj.login("小明")
# obj.logout(obj)
# print(obj.name)

# demo = __import__("Scripts.Util.logger", fromlist=['logger'])
# obj = getattr(demo, 'Log')
# obj().warning("还有谁")
import json

# demo = {'0': {'username': 'admin', 'password': '123456', '*': 'username,password,age', 'age': 18}}
# demo1 = {'0': {'username': 'admin', 'password': '123456', '?': 'username,password,age', 'age': 20}}
#
# def dynamic_case(case_dict):
#     flag = 0
#     res_dict = {}
#     for i in case_dict.values():
#         i_json = json.dumps(i)
#         if "*" in i:
#             res = i['*'].split(',')
#             i.pop('*')
#             for key in res:
#                 a = json.loads(i_json)
#                 a.pop(key)
#                 res_dict[str(flag)] = a
#                 flag += 1
#         elif "?" in i:
#             res = i['?'].split(',')
#             i.pop('?')
#             for key in res:
#                 a = json.loads(i_json)
#                 a[key] = ''
#                 res_dict[str(flag)] = a
#                 flag += 1
#
#     for i in res_dict.values():
#         if "*" in i:
#             i.pop("*")
#         else:
#             i.pop("?")
#
#     return res_dict
#
#
# print(dynamic_case(demo))
# print(dynamic_case(demo1))
