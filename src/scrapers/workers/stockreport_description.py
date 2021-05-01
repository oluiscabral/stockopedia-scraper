from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from data_structure.scraped import Scraped
from scrapers import common
from data_structure.data_ref import DataRef


class StockReportDescription(ScraperComponent):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = Scraped(self.name, wd, ref)
        rows = wd.find_elements_by_css_selector(".stockreport-header__table tbody tr")
        common.lines_by_tag(rows, 'td', data)
        return {data}
