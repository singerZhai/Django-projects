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


# import requests
#
# url = "https://gateway.qschou.com/v3.0.0/passport/sms/login"
# data = {
#     "phone": "15611066631",
#     "country": "86",
#     "sms_code": "9527",
#     "platform": "wxh5"
# }
#
# r = requests.post(url=url, data=data)
#
# print(r.json())


# import collections
# import random
#
# Card = collections.namedtuple('Card', ['rank', 'suit'])
#
#
# class FrenchDeck:
#     ranks = [str(n) for n in range(2, 11)] + list('JQKA')
#     suits = 'spades diamonds clubs hearts'.split()
#
#     def __init__(self):
#         self._card = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
#
#     def __len__(self):
#         return len(self._card)
#
#     def __getitem__(self, position):
#         return self._card[position]


# french_deck = FrenchDeck()
# print(french_deck.ranks)
# print(french_deck.suits)
# card = Card(123, 'hello')
# print(len(french_deck))
# print(french_deck._card)
# print(french_deck[0])
# print(french_deck[-1])
# print(random.choice(french_deck))
# for card in french_deck:
#     print(card)
# for card in reversed(french_deck):
#     print(card)
# print(Card('2', 'clubs') in french_deck)
# suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
#
#
# def spades_high(card):
#     rank_value = FrenchDeck.ranks.index(card.rank)
#     return rank_value * len(suit_values) + suit_values[card.suit]
#
# for card in sorted(french_deck, key=spades_high):
#     print(card)

# from math import hypot
#
# class Vector:
#
#     def __init__(self, x=0, y=0):
#         self.x = x
#         self.y = y
#
#     def __repr__(self):
#         return 'Vector(%r, %r)' % (self.x, self.y)
#
#     def __abs__(self):
#         return hypot(self.x, self.y)
#
#     def __bool__(self):
#         return bool(abs(self))
#
#     def __add__(self, other):
#         x = self.x + other.x
#         y = self.y + other.y
#         return Vector(x, y)
#
#     def __mul__(self, other):
#         return Vector(self.x * scalar, self.y * scalar)
# import requests
# from requests.exceptions import InvalidSchema
#
# url = "123452524"
# data = {'username': 'admin', 'password': '123456'}
# try:
#     r = requests.post(url, data)
# except Exception:
#     print("demo")

# a = '123'
# print(isinstance(1, type))

# demo = '123'
# print(callable(print))
import os

path = os.getcwd()
print(path)