'''
@author: oluiscabral
'''
from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from scrapers import common
from data_structure.data_ref import DataRef


class StockReportSummary(ScraperComponent):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = common.init_data('Financial Summary', self.name, wd, ref)
        tables = wd.find_elements_by_css_selector("stockreport-financial-summary")
        for table in tables:
            self.scrap_table(data, table)
        return {data}

    def scrap_table(self, data, table):
        common.scrap_ths(data, table)
        trs = table.find_elements_by_css_selector('tbody tr')
        common.lines_by_tag(trs, 'td', data)
