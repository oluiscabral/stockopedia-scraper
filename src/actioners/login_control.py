'''
@author: oluiscabral
'''
from actioners.interfaces.i_login_control import ILoginControl
from actioners.navigator import Navigator
import time

class LoginControl(ILoginControl):
    def __init__(self, wd, login_ui):
        self.wd = wd
        self.login_ui = login_ui
        self.login_page_url = "https://www.stockopedia.com/auth/login/"
        self.app_page_url = "https://app.stockopedia.com/"
    
    def __in_login_page(self):
        url = self.wd.current_url
        return url.startswith(self.login_page_url)

    def __get_username_and_password_from_ui(self):
        username = self.login_ui.get_username()
        password = self.login_ui.get_password()
        return username, password

    def __fill_element_fields(self, username_element, password_element, username, password):
        username_element.clear()
        password_element.clear()
        username_element.send_keys(username)
        password_element.send_keys(password)

    def __try_login(self, username_element, password_element, submit_element):
        username, password = self.__get_username_and_password_from_ui()
        self.__fill_element_fields(username_element, password_element, username, password)
        self.login_ui.display_login_action_message()
        submit_element.click()

    def __find_login_elements(self):
        username_element = self.wd.find_element_by_name('username')
        password_element = self.wd.find_element_by_name('password')
        submit_element = self.wd.find_element_by_id('auth_submit')
        return username_element, password_element, submit_element

    def __in_app_page(self):
        url = self.wd.current_url
        return url.startswith(self.app_page_url)
    
    def __logged_in(self):
        if self.__in_app_page():
            return True
        return False
        
    def __get_try_login_result(self):
        time.sleep(2)
        if self.__logged_in():
            self.login_ui.display_login_success_message()
            return True
        self.login_ui.display_login_fail_message()
        return False

    def force_login(self):
        if self.__logged_in():
            return None
        if not self.__in_login_page():
            Navigator.get(self.wd, self.login_page_url)
        try_login_result = False
        while not try_login_result:
            username_element, password_element, submit_element = self.__find_login_elements()
            self.__try_login(username_element, password_element, submit_element)
            try_login_result = self.__get_try_login_result()
