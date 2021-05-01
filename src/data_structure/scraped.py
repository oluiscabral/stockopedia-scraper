'''
@author: oluiscabral
'''
from typing import Iterable
from data_structure.data import Data
from data_structure.data_ref import DataRef
from selenium.webdriver.remote.webdriver import WebDriver

class Scraped(Data):
    def __init__(self, name:str, wd:WebDriver, ref:DataRef):
        super().__init__(name, ref)
        self.wd = wd
    
    def append_line(self, line:Iterable[str]):
        self.table.append(list(line))
    