from selenium.webdriver.remote.webdriver import WebDriver
from webpage import Webpage
from scraped_data import ScrapedData
from bs4 import BeautifulStoneSoup
import typing

class StockopediaCompareWebpage(Webpage):
    def __init__(self, webdriver: WebDriver, base_url:str, stock_tickers:typing.List[str]):
        self.base_url = base_url
        self.stock_tickers = stock_tickers
        url = base_url + 'compare?tickers='+ ','.join(stock_tickers)
        super().__init__(webdriver, url, 30)
    
    def scrap(self) -> ScrapedData:
        ret = ScrapedData()
        soup = self.soup
        main = ret.main
        table:BeautifulStoneSoup = soup.find('table', attrs={'id':'compareTable'})
        if table == None:
            return None
        tbody = table.findChildren('tbody')[0]
        main['tbody'] = tbody
        main['url'] = self.url
        main['time-stamp'] = self.time_stamp
        main['stock-tickers'] = self.stock_tickers
        return ret
