'''
@author: oluiscabral
'''
from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from data_structure.scraped import Scraped
from data_structure.data_ref import DataRef


class CompareTable(ScraperComponent):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = Scraped(self.name, wd, ref)
        table = wd.find_element_by_css_selector('table#compareTable')
        thead_ths = table.find_elements_by_css_selector('thead tr th')
        self.scrap_th(data, thead_ths)
        trs = table.find_elements_by_css_selector('tbody tr')
        for tr in trs:
            self.scrap_tr(data, tr)
        return {data}

    def scrap_th(self, data, ths):
        line = []
        for th in ths:
            label = th.get_attribute('aria-label')
            if label == None:
                label = th.text
            line.append(label.strip())
        data.append_line(line)

    def scrap_tr(self, data, tr):
        tds = tr.find_elements_by_tag_name('td')
        line = [td.text.strip() for td in tds]
        data.append_line(line)
