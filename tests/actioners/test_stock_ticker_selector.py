'''
Created on Apr 18, 2021

@author: oluiscabral
'''
import unittest
from helpers.webdriver_factory import WebdriverFactory
from ui.login_ui import LoginUI
from ui.stock_ticker_selector_ui import StockTickerSelectorUI
from actioners.login_control import LoginControl
from actioners.stock_ticker_selector import StockTickerSelector


class Test(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.wd = WebdriverFactory.create()
        login_control = LoginControl(cls.wd, LoginUI())
        login_control.force_login()
        cls.ui = StockTickerSelectorUI()
        
    def test_get_selected_stock_ticker(self):
        stock_ticker_selector = StockTickerSelector(Test.wd, Test.ui)
        selected_stock_ticker = stock_ticker_selector.get_selected_stock_ticker()
        print(selected_stock_ticker)
        self.assertNotEqual(None, selected_stock_ticker)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()