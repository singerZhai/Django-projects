from FirstApp.util import *


class Msg:

    def __init__(self):
        self.msg = {
            "login_200": {
                "error_code": "200",
                "msg": "登录成功",
                "userToken": Util().userToken()
            },
            "sign_in_200": {
                "error_code": "200",
                "msg": "注册成功"
            },
            "change_password_200": {
                "error_code": "200",
                "msg": "密码修改成功"
            },
            "2001": {
                "error_code": "2001",
                "msg": "参数不合法"
            },
            "2002": {
                "error_code": "2002",
                "msg": "用户名不能为空"
            },
            "2003": {
                "error_code": "2003",
                "msg": "密码不能为空"
            },
            "2004": {
                "error_code": "2004",
                "msg": "用户名已注册"
            },
            "2005": {
                "error_code": "2005",
                "msg": "用户名最长16位"
            },
            "2006": {
                "error_code": "2006",
                "msg": "密码最长16位"
            },
            "300": {
                "error_code": "300",
                "msg": "系统繁忙"
            },
            "2007": {
                "error_code": "2007",
                "msg": "密码错误"
            },
            "2008": {
                "error_code": "2008",
                "msg": "用户未注册"
            },
            "2009": {
                "error_code": "2009",
                "msg": "token 无效"
            }
        }