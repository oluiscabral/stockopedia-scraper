'''
@author: oluiscabral
'''
from abc import ABC, abstractmethod
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from data_structure.data_ref import DataRef

class ScraperComponent(ABC):
    def __init__(self, name:str):
        self.name = name
    
    @abstractmethod
    def scrap(self, wd:WebDriver, ref:DataRef)->Set[Data]:
        pass