'''
@author: oluiscabral
'''
from selenium.webdriver.remote.webdriver import WebDriver
import time

class Navigator:
    @staticmethod
    def get(wd:WebDriver, url:str, count:int=5)->bool:
        wd.get(url)
        time.sleep(count)
        if wd.current_url.startswith(url):
            return True
        return False