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


class StockReportActivity(ScraperComponent, object):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = common.init_data('Shareholder Activity', self.name, wd, ref)
        tables = wd.find_elements_by_css_selector("stockreport-shareholder-activity")
        for table in tables:
            self.scrap_table(data, table)
        return {data}

    def scrap_table(self, data, table):
        common.scrap_ths(data, table)
        trs = table.find_elements_by_css_selector('tbody tr')
        for tr in trs:
            self.scrap_tr(data, tr)

    def scrap_tr(self, data, tr):
        tds = tr.find_elements_by_tag_name('td')
        line = [tds[0].text.strip()]
        parts: WebElement = tds[1].find_elements_by_css_selector('split-bar span span')
        for part in parts:
            self.scrap_part(line, part)
        data.append_line(line)

    def scrap_part(self, line, part):
        style = part.get_property('style')
        n = style['WebkitFlexGrow']
        line.append(n)
