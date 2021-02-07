from selenium.webdriver.remote.webdriver import WebDriver
import typing

def get_value(web_driver_func, ref:str) -> str:
    try:
        return web_driver_func(ref).strip()
    except Exception:
        return None

def get_element(web_driver_func, ref:str) -> WebDriver:
    try:
        return web_driver_func(ref)
    except Exception:
        return None

def get_elements(web_driver_func, ref:str) -> typing.List[WebDriver]:
    try:
        return web_driver_func(ref)
    except Exception:
        return None

def get_element_by_id(web_driver:WebDriver, element_id:str) -> WebDriver:
    return get_element(web_driver.find_element_by_id, element_id)

def get_element_by_name(web_driver:WebDriver, name:str) -> WebDriver:
    return get_element(web_driver.find_element_by_name, name)

def get_element_by_css_selector(web_driver:WebDriver, css_selector:str) -> WebDriver:
    return get_element(web_driver.find_element_by_css_selector, css_selector)

def get_elements_by_tag(web_driver:WebDriver, tag:str) -> WebDriver:
    return get_elements(web_driver.find_elements_by_tag_name, tag)

def get_elements_by_css_selector(web_driver:WebDriver, css_selector:str) -> typing.List[WebDriver]:
    return get_elements(web_driver.find_elements_by_css_selector, css_selector)

def get_attribute(web_driver:WebDriver, name:str) -> str:
    return get_value(web_driver.get_attribute, name)