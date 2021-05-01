'''
@author: oluiscabral
'''
from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from data_structure.scraped import Scraped
from data_structure.data_ref import DataRef


class StockReportSimilar(ScraperComponent):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = Scraped(self.name, wd, ref)
        divs = wd.find_elements_by_css_selector("stockreport-similar div div .related__item-column--name")
        line = []
        for div in divs:
            self.scrap_div(line, div)
        data.append_line(line)
        return {data}

    def extract_stock_ticker_rep(self, a_href: str) -> str:
        rep_init = a_href.rfind('-') + 1
        return a_href[rep_init:len(a_href)]

    def scrap_div(self, line, div):
        a = div.find_element_by_tag_name('a')
        a_href = a.get_attribute('href')
        a_stock_ticker = self.extract_stock_ticker_rep(a_href)
        line.append(a_stock_ticker)
