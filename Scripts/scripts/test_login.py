from time import sleep
import requests
import unittest
from Scripts.Util.logger import Log
from Scripts.Util.util import Base, Conf


class TestLogin(unittest.TestCase):

    def setUp(self) -> None:
        self.logger = Log()
        self.logger.debug("begin")

    def test_login(self):
        url = Conf.msg['login']
        all_data = Base().read_ini_case("login")
        for i in all_data.values():
            # print(i)
            r = requests.post(url, i)
            print(r.text)
            # sleep(1)

    def tearDown(self) -> None:
        self.logger.debug("end")
