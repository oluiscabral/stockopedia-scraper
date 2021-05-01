'''
@author: oluiscabral
'''
import unittest
from helpers.webdriver_factory import WebdriverFactory
from selenium.webdriver.remote.webdriver import WebDriver


class Test(unittest.TestCase):
    def test_create(self):
        wd = WebdriverFactory.create()
        
        self.assertIsInstance(wd, WebDriver)
        
        wd.close()
        wd = None


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()