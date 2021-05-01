'''
@author: oluiscabral
'''
from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from data_structure.scraped import Scraped
from data_structure.data_ref import DataRef


class StockReportMeter(ScraperComponent):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = Scraped(self.name, wd, ref)
        meters = wd.find_elements_by_tag_name('stockreport-meter')
        for meter in meters:
            self.scrap_meter(data, meter)
        return {data}

    def scrap_meter(self, data, meter):
        line = []
        h5 = meter.find_element_by_css_selector('div div h5')
        line.append(h5.text.strip())
        chip = meter.find_element_by_css_selector('div div .chip')
        line.append(chip.text.strip())
        data.append_line(line)
