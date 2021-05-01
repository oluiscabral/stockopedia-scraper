'''
@author: oluiscabral
'''
from actioners.interfaces.i_login_control import ILoginControl
from scrapers.composites.scraper_composite import ScraperComposite
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from scrapers.workers.stockreport_similar import StockReportSimilar
from data_structure.data_ref import DataRef
from scrapers.url import URL

class CompareScraper(ScraperComposite):
    def __init__(self, name:str, url:URL, login_control:ILoginControl):
        super().__init__(name, url, login_control)
        self.create_stockreport_scraper()
    
    def scrap(self, wd:WebDriver, ref:DataRef)->Set[Data]:
        self.set_url_ref(wd, ref)
        return ScraperComposite.scrap(self, wd, ref)

    def set_url_ref(self, wd, ref):
        stock_tickers_data = self.stock_report_scraper.scrap(wd, ref).pop()
        url_ref = self.extract_stock_tickers(stock_tickers_data)
        ref.set_url_ref(url_ref)
        
    def extract_stock_tickers(self, stock_tickers_data:Data):
        line = stock_tickers_data.get()[0]
        return ','.join(line)
    
    def create_stockreport_scraper(self):
        stockreport_scraper = ScraperComposite('stockreport', URL('https://app.stockopedia.com/share-prices/${}'), self.login_control)
        stockreport_scraper.add_children(StockReportSimilar('stockreport-similar'))
        self.stock_report_scraper = stockreport_scraper


