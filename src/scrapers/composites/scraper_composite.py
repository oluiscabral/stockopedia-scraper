'''
@author: oluiscabral
'''
from scrapers.composites.base_composite import BaseComposite
from data_structure.data import Data
from typing import Set
from selenium.webdriver.remote.webdriver import WebDriver
from actioners.interfaces.i_login_control import ILoginControl
from actioners.navigator import Navigator
from data_structure.data_ref import DataRef
from scrapers.url import URL

class ScraperComposite(BaseComposite):
    def __init__(self, name:str, url:URL, login_control:ILoginControl):
        super().__init__(name)
        self.url = url
        self.login_control = login_control
    
    def get_url(self, ref:DataRef)->str:
        url_ref = ref.get_url_ref()
        return self.url.get(url_ref)
    
    def scrap(self, wd:WebDriver, ref:DataRef)->Set[Data]:
        self.login_control.force_login()
        if Navigator.get(wd, self.get_url(ref)):
            return BaseComposite.scrap(self, wd, ref)
        return set()