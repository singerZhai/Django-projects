from parameterized import parameterized
import unittest
from Scripts.Util.util import Util
from Scripts.Util.logger import Log
from Scripts.Util.util import Conf


class TestLogin(unittest.TestCase):

    count = 1

    def setUp(self) -> None:
        self.logger = Log()
        self.logger.debug("begin")

    @parameterized.expand(Util.get_json("login"))
    def test_login(self, *args):
        data = dict(args)
        url = Conf.msg['login']
        res = Util.send_requests(url, data=data, method='post')
        Util.write_static_files(res, 5)
        # Util.assert_equal()

    def tearDown(self) -> None:
        self.logger.debug("end")
