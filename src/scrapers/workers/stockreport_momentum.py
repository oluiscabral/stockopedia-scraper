'''
@author: oluiscabral
'''
from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from scrapers import common
from data_structure.data_ref import DataRef


class StockReportMomentum(ScraperComponent):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = common.init_data('Momentum', self.name, wd, ref)
        tables = wd.find_elements_by_css_selector("stockreport-ratios.momentumComp table")
        for table in tables:
            self.scrap_table(data, table)
        return {data}

    def scrap_table(self, data, table):
        thead = table.find_element_by_tag_name('thead')
        data.append_line([thead.text])
        trs = table.find_elements_by_css_selector('tbody tr')
        for tr in trs:
            self.scrap_tr(data, tr)

    def scrap_tr(self, data, tr):
        line = []
        tds = tr.find_elements_by_tag_name('td')
        for td in tds[:2]:
            line.append(td.text.strip())
        icon_selection: WebElement = tds[2].find_element_by_css_selector('.lotto')
        icon_rep = common.lotto_icon_rep(icon_selection)
        line.append(icon_rep)
        data.append_line(line)
