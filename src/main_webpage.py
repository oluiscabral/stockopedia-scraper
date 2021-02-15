from selenium.webdriver.remote.webdriver import WebDriver
from webpage import Webpage
from scraped_data import ScrapedData, MainScrapedData
from compare_webpage import StockopediaCompareWebpage

class StockopediaMainWebpage(Webpage):
    def __init__(self, webdriver: WebDriver, base_url:str, rel_url:str):
        self.base_url = base_url
        self.name = rel_url
        url = base_url + 'share-prices/'+rel_url
        super().__init__(webdriver, url, 20)
        self.translator = {
            'desc': '.stockreport-header__table tbody tr',
            'momentum': 'stockreport-ratios.momentumComp',
            'ranks': 'stockreport-ranks .ranks div.ranks__line',
            'gv': 'stockreport-ratios.valueComp',
            'summary': 'stockreport-financial-summary',
            'meters': 'stockreport-meter',
            'other-ratios': 'stockreport-other-ratios'
            }
    
    def scrap(self)-> ScrapedData:
        ret = MainScrapedData()
        soup = self.soup
        translator = self.translator
        compare = self.scrap_similars()
        if compare != None:
            ret.compare = compare.main
        main = ret.main
        main['name'] = self.name
        main['time-stamp'] = self.time_stamp
        main['url'] = self.url
        for code in translator:
            main[code] = soup.select(translator[code])
        main['quality'] = soup.find('stockreport-ratios', attrs={'viewkey':'quality'})
        main['recent-story'] = soup.find('stockreport-ratios', attrs={'viewname':'stockreport_recent_history'})
        return ret
    
    def scrap_similars(self)->ScrapedData:
        webdriver = self.webdriver
        soup = self.soup
        a_elements = soup.find_all('a', attrs={'uisref': 'app.shr-report.report'})
        if len(a_elements) == 0:
            return None
        stock_tickers = []
        for a_element in a_elements:
            stock_tickers.append(self.get_stock_ticker(a_element['href']))
        compare_webpage = StockopediaCompareWebpage(webdriver, self.base_url, stock_tickers)
        return compare_webpage.scrap()
    
    def get_stock_ticker(self, s:str) -> str:
        length = len(s)
        for i, c in enumerate(reversed(s)):
            if c != ':' and not c.isupper():
                break
        return s[length - i:length]
            
        