from selenium.webdriver.remote.webdriver import WebDriver
import webdriver_utils
import webdriver_factory
from main_webpage import StockopediaMainWebpage
import time

class StockopediaWebsite:
    base_url = 'https://app.stockopedia.com/'
    login_url = 'https://www.stockopedia.com/auth/login/'

    def __init__(self):
        self.wd: WebDriver = webdriver_factory.get_webdriver()
        self.logged_in = False

    def login(self, username:str, password:str):
        if self.logged_in:
            return True
        wd = self.wd
        wd.get(StockopediaWebsite.login_url)
        username_input = webdriver_utils.get_element_by_id(wd,'username')
        password_input = webdriver_utils.get_element_by_id(wd,'password')
        submit_button = webdriver_utils.get_element_by_id(wd,'auth_submit')
        username_input.send_keys(username)
        password_input.send_keys(password)
        submit_button.click()
        if wd.current_url.startswith(StockopediaWebsite.login_url):
            message_divs = wd.find_elements_by_css_selector('div.ui.red.message div')
            if len(message_divs) > 0:
                print('Exception: '+ message_divs[0].text.strip())
            else:
                print('Execption: could not login at Stockopedia.')
            return False
        print('Succefully logged in Stockopedia!')
        self.logged_in = True
        return True
                
    def get_main_webpage(self, stock_ticker:str) -> StockopediaMainWebpage:
        if self.logged_in:
            wd = self.wd
            wd.get(StockopediaWebsite.base_url)
            search_input = webdriver_utils.get_element_by_name(wd, 'searchQuery')
            search_input.send_keys(stock_ticker)
            time.sleep(10)
            result = webdriver_utils.get_element_by_css_selector(wd, 'div.result.item.result-security.ng-star-inserted.active')
            if result == None:
                return None
            data_param = webdriver_utils.get_attribute(result, 'data-param')
            if data_param == None:
                return None
            return StockopediaMainWebpage(wd, StockopediaWebsite.base_url, data_param)
    