'''
@author: oluiscabral
'''
from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from scrapers import common
from data_structure.data_ref import DataRef


class StockReportRatios(ScraperComponent):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = common.init_data('Other ratios', self.name, wd, ref)
        tables = wd.find_elements_by_css_selector("stockreport-other-ratios table")
        for table in tables:
            self.scrap_table(data, table)
        return {data}

    def scrap_table(self, data, table):
        common.scrap_ths(data, table)
        trs = table.find_elements_by_css_selector('tbody tr')
        for tr in trs:
            line = self.scrap_tr(tr)
            data.append_line(line)

    def scrap_tr(self, tr):
        tds = tr.find_elements_by_tag_name('td')
        line = []
        for td in tds:
            self.scrap_td(line, td)
        return line

    def scrap_td(self, line, td):
        t = td.text.strip()
        if t:
            line.append(t)
        else:
            icon_rep = ''
            try:
                icon = td.find_element_by_css_selector('.lotto')
                icon_rep = common.lotto_icon_rep(icon)
            except Exception:
                pass
            line.append(icon_rep)
