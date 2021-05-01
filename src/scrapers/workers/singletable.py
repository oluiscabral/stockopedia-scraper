'''
@author: oluiscabral
'''
from scrapers.interfaces.scraper_component import ScraperComponent
from typing import List, Set
from selenium.webdriver.remote.webelement import WebElement
from data_structure.data import Data
from selenium.webdriver.remote.webdriver import WebDriver
from data_structure.scraped import Scraped
from data_structure.data_ref import DataRef


class SingleTable(ScraperComponent):
    def __init__(self, name: str):
        ScraperComponent.__init__(self, name)

    def scrap(self, wd: WebDriver, ref: DataRef) -> Set[Data]:
        data = Scraped(self.name, wd, ref)
        header, body = self.get_header_and_body(wd)
        header_contents = self.get_header_contents(header)
        body_contents = self.get_body_contents(body)
        data.append_line(header_contents)
        for line in body_contents:
            data.append_line(line)
        return {data}

    def get_header_contents(self, header: WebElement) -> List[str]:
        ret = ['']
        ths = header.find_elements_by_css_selector('th.data-table__table-header')
        for th in ths:
            ret.append(th.text.strip())
        return ret

    def get_left_body_contents(self, left_body: WebElement) -> List[List[str]]:
        ret = []
        trs = left_body.find_elements_by_css_selector('.data-table__row')
        for tr in trs:
            tds = tr.find_elements_by_tag_name('td')
            line = [td.text.strip() for td in tds]
            ret.append(line)
        return ret

    def get_right_body_contents(self, right_body: WebElement) -> List[List[str]]:
        ret = []
        table = right_body.find_element_by_tag_name('table')
        ths = table.find_elements_by_css_selector('thead tr th')
        ret.append([th.text.strip() for th in ths])
        trs = table.find_elements_by_css_selector('tbody tr')
        for tr in trs:
            tds = tr.find_elements_by_tag_name('td')
            ret.append([td.text.strip() for td in tds])
        return ret

    def get_body_contents(self, body: WebElement) -> List[List[str]]:
        ret: List[List[str]] = []
        left_body = body.find_element_by_css_selector('div.data-table__pinned')
        right_body = body.find_element_by_css_selector('div.data-table__data')
        left_body_contents = self.get_left_body_contents(left_body)
        right_body_contents = self.get_right_body_contents(right_body)[2:]
        for i in range(len(left_body_contents)):
            line = left_body_contents[i].copy()
            line.extend(right_body_contents[i])
            ret.append(line)
        return ret

    def get_header_and_body(self, wd):
        table = wd.find_element_by_css_selector('statement-table .data-table')
        header = table.find_element_by_class_name('data-table__header')
        body = table.find_element_by_class_name('data-table__tables')
        return header, body
