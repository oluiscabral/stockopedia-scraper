'''
@author: oluiscabral
'''
from helpers.webdriver_factory import WebdriverFactory
from actioners.login_control import LoginControl
from ui.login_ui import LoginUI
import unittest


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd = WebdriverFactory.create(False)
        cls.login_ui = LoginUI()
    
    @classmethod
    def tearDownClass(cls):
        cls.wd.close()
        cls.wd = None
        cls.login_ui = None
        
    def check_login(self):
        url = Test.wd.current_url
        return not url.startswith("https://www.stockopedia.com/auth/login/")
    
    def test_login(self):
        login_control = LoginControl(Test.wd, Test.login_ui)
        login_control.force_login()
        self.assertEqual(True, self.check_login())
        
if __name__ == "__main__":
    unittest.main()