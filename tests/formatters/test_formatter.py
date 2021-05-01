'''
@author: oluiscabral
'''
import unittest
from formatters.formatter import Formatter, FormatInfo
from data_structure.data_ref import DataRef
from templates.template import Template
from creationals.scraper_factory import ScraperFactory
from scrapers.composites.base_composite import BaseComposite
from helpers.webdriver_factory import WebdriverFactory
from actioners.login_control import LoginControl
from ui.login_ui import LoginUI
from scrapers.names import STOCKREPORT_DESCRIPTION

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
        cls.login_control = None
    
    def test_formatter(self):
        base_scraper = BaseComposite('main')
        stockreport_scraper = ScraperFactory.create('stockreport', Test.login_control)
        base_scraper.add_children(stockreport_scraper)
        result = base_scraper.scrap(Test.wd, DataRef('csl-ASX:CSL'))
        
        data_ref = DataRef('csl-ASX:CSL', ['main', 'stockreport', STOCKREPORT_DESCRIPTION])
        definition = {
            data_ref: (0,1)
        }
        template = Template(definition)
        formatter = Formatter(template)
        
        data = formatter.format(result, FormatInfo('Stockreport', 20, 20, DataRef('csl-ASX:CSL', ['main'])))
        
        self.assertEqual(20, len(data.get()))
        
        for line in data:
            print(line)
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()