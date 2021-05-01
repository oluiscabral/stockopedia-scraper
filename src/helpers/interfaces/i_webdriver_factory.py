'''
@author: oluiscabral
'''
import abc
from selenium.webdriver.remote.webdriver import WebDriver

class IWebdriverFactory(abc.ABC):
    @abc.abstractstaticmethod
    def create(headless:bool=True)->WebDriver:  # @NoSelf
        pass