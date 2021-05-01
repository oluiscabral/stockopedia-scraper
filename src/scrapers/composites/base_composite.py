'''
@author: oluiscabral
'''
from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from data_structure.data_ref import DataRef
import time

class BaseComposite(ScraperComponent):
    def __init__(self, name:str):
        super().__init__(name)
        self.children:Set[ScraperComponent] = set()
    
    def add_children(self, c:ScraperComponent):
        self.children.add(c)
        
    def remove_children(self, c:ScraperComponent):
        self.children.remove(c)
        
    def scrap(self, wd:WebDriver, ref:DataRef)->Set[Data]:
        print("Scraping", self.name)
        result:Set[Data] = set()
        cref = ref.clone()
        cref.add_owner(self.name)
        for c in self.children:
            try:
                result.update(c.scrap(wd, cref))
            except Exception:
                time.sleep(5)
                try:
                    result.update(c.scrap(wd, cref))
                except Exception:
                    pass
        ref.reset()
        return result