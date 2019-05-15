# -*- coding: utf-8 -*-
# @Author  : 翟会德
# @Time    : 2019-05-05 15:07
# @File    : demo.py
# @Software: PyCharm
import os

path = os.getcwd()
# print(path)
# os.makedirs(path + "/demo.txt")

new_path_filename = path + "/demo.txt"
os.system(r'touch %s' % new_path_filename)