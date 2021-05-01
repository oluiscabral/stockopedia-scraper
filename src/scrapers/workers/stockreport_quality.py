'''
@author: oluiscabral
'''
from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from scrapers import common
from data_structure.data_ref import DataRef


class StockReportQuality(ScraperComponent):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = common.init_data('Quality', self.name, wd, ref)
        tag = common.get_tag(wd, 'stockreport-ratios', 'viewkey', 'quality')
        tables = tag.find_elements_by_tag_name('table')
        for table in tables:
            common.DataWithProgressBar.scrap(data, table)
        return {data}
