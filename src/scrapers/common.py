'''
@author: oluiscabral
'''
from typing import Iterable
from selenium.webdriver.remote.webelement import WebElement
from data_structure.scraped import Scraped
from selenium.webdriver.remote.webdriver import WebDriver


class DataWithProgressBar:
    @staticmethod
    def scrap(data, table):
        DataWithProgressBar.scrap_ths(data, table)
        trs = table.find_elements_by_css_selector('tbody tr')
        for tr in trs:
            DataWithProgressBar.scrap_tr(data, tr)
    @staticmethod
    def scrap_ths(data, table):
        ths = table.find_elements_by_css_selector('thead tr th')
        line = [th.text.strip() for th in ths]
        data.append_line(line)
    
    @staticmethod
    def scrap_tr(data, tr):
        tds = tr.find_elements_by_tag_name('td')
        f = tds[0].text.strip()
        line = f.splitlines()
        for td in tds[1:]:
            DataWithProgressBar.scrap_td(line, td)
        data.append_line(line)
    
    @staticmethod
    def scrap_td(line, td):
        graphs = td.find_elements_by_css_selector('percent-progress .bar')
        for graph in graphs:
            graph: WebElement
            style = graph.get_property('style')
            n = style['width']
            line.append(n)

def lines_by_tag(iterable:Iterable[WebElement], tag:str, data:Scraped):
        for item in iterable:
            sel = item.find_elements_by_tag_name(tag)
            line = [s.text.strip() for s in sel]
            data.append_line(line)

def lotto_icon_rep(element:WebDriver):
        class_attribute = element.get_attribute('class')
        class_values = [stmt for stmt in class_attribute.split() if stmt.startswith('lotto--') and stmt != 'lotto--xs']
        if len(class_values) > 0:
            return class_values[0]
        return ''

def scrap_ths(data, table):
    ths = table.find_elements_by_css_selector('thead tr th')
    line = [th.text.strip() for th in ths]
    data.append_line(line)

def init_data(title, name, wd, ref):
    data = Scraped(name, wd, ref)
    data.append_line([title])
    return data

def get_tag(wd, selector, attr_name, search):
    tags = wd.find_elements_by_css_selector(selector)
    for tag in tags:
        compare = tag.get_attribute(attr_name)
        if compare == search:
            break
    return tag
