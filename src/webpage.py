from selenium.webdriver.remote.webdriver import WebDriver
from datetime import datetime
import pytz
import abc
from scraped_data import ScrapedData
from bs4 import BeautifulSoup
import time

class Webpage:
    def __init__(self, webdriver: WebDriver, url:str, t:int):
        self.webdriver = webdriver
        webdriver.get(url)
        time.sleep(t)
        self.time_stamp = datetime.now(pytz.timezone('Australia/Sydney'))
        self.url = url
        self.soup = BeautifulSoup(webdriver.page_source, 'html.parser')
    
    @abc.abstractclassmethod
    def scrap(self) -> ScrapedData:
        raise NotImplementedError
