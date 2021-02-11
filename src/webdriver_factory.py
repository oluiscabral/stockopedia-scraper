from selenium.webdriver.remote.webdriver import WebDriver
from config import Config
from selenium import webdriver

class Browser:
    def __init__(self, wd:WebDriver, exec_path:str, options):
        self.wd = wd
        self.exec_path = exec_path
        self.options = options

def get_webdriver() -> WebDriver:
    plat = Config.platform
    sep = get_sys_sep(plat)
    base_path = '..'+sep+'webdrivers'+sep
    possible_browsers = [
        Browser(webdriver.Chrome, base_path+'chromedriver'+sep, webdriver.ChromeOptions()),
        Browser(webdriver.Firefox, base_path+'geckodriver'+sep, webdriver.FirefoxOptions())
    ]
    for browser in possible_browsers:
        try:
            return get_webdriver_to_os(browser, plat)
        except Exception:
            pass
    return None

def get_sys_sep(plat:str) -> str:
    sep = '/'
    if plat == 'WIN32':
        sep = '\\'
    return sep

def get_webdriver_to_os(browser:Browser, plat:str) -> WebDriver:
    web_driver = browser.wd
    exec_path = browser.exec_path
    options = browser.options
    options.set_headless()
    if plat == 'LINUX' or plat == 'LINUX2':
        ret = web_driver(executable_path=exec_path+'linux', options=options)
    elif plat == 'DARWIN':
        ret = web_driver(executable_path=exec_path+'darwin', options=options)
    elif plat == 'WIN32':
        ret = web_driver(executable_path=exec_path+'win.exe', options=options)
    ret.implicitly_wait(30)
    return ret
