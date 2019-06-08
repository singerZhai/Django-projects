from parameterized import parameterized
import unittest
from Scripts.Util.util import Util
from Scripts.Util.logger import Log


class TestLogin(unittest.TestCase):

    global logger

    @classmethod
    def setUpClass(cls):

        cls.logger = Log()
        cls.logger.debug("begin")

    @parameterized.expand(Util.get_json("login"))
    def test_login(self, *args):
        data = dict(args)
        response = Util.send_request('login', data, 'POST')
        Util.write_static_files(response, 5)

    @classmethod
    def tearDownClass(cls):
        Util.assert_equal('test_login')
        cls.logger.wairning("end")
