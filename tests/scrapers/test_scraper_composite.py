'''
@author: oluiscabral
'''
import unittest
from creationals.scraper_factory import ScraperFactory
from helpers.webdriver_factory import WebdriverFactory
from actioners.login_control import LoginControl
from ui.login_ui import LoginUI
from data_structure.data_ref import DataRef

class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd = WebdriverFactory.create()
        cls.login_control = LoginControl(cls.wd, LoginUI())
        cls.login_control.force_login()
    
    @classmethod
    def tearDownClass(cls):
        cls.wd.close()
        cls.wd = None
    
    def test_stockreport(self):
        stockreport_scraper = ScraperFactory.create('stockreport', Test.login_control)
        result = stockreport_scraper.scrap(Test.wd, DataRef('csl-ASX:CSL'))
        self.assertEqual(11, len(result))
    
    def test_compare(self):
        compare_scraper = ScraperFactory.create('compare', Test.login_control)
        result = compare_scraper.scrap(Test.wd, DataRef('csl-ASX:CSL'))
        self.assertEqual(1, len(result))
    
    def test_singletable(self):
        balance_scraper = ScraperFactory.create('balance', Test.login_control)
        result=balance_scraper.scrap(Test.wd, DataRef('csl-ASX:CSL'))
        self.assertEqual(1, len(result))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()