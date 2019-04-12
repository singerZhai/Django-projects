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


demo = '"BxGAbKiDVNi5MWlaOgzIASgsBeuTHg"'
res = demo.replace('"', '')
print(res)