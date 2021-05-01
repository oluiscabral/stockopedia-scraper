'''
@author: oluiscabral
'''
from actioners.interfaces.i_stock_ticker_selector import IStockTickerSelector
import time
from actioners.navigator import Navigator

class StockTickerSelector(IStockTickerSelector):
    def __init__(self,wd, stock_ticker_selector_ui):
        self.wd = wd
        self.stock_ticker_selector_ui = stock_ticker_selector_ui

    def __fill_searcher_element(self, searcher_element, search_value):
        searcher_element.clear()
        searcher_element.send_keys(search_value)

    def __get_searcher_element_results(self):
        results = []
        result_elements = self.wd.find_elements_by_css_selector('div.result.item.result-security')
        for element in result_elements:
            attr = str(element.get_attribute('data-param'))
            if attr is None or not attr.strip():
                continue
            results.append(attr)
        return results
    
    def __get_stock_ticker_options(self, searcher_element, search_value):
        self.__fill_searcher_element(searcher_element, search_value)
        time.sleep(2)
        return self.__get_searcher_element_results()
    
    def get_selected_stock_ticker(self)->str:
        Navigator.get(self.wd, "https://app.stockopedia.com/home")
        searcher_element = self.wd.find_element_by_name('searchQuery')
        while True:
            search_value = self.stock_ticker_selector_ui.get_search_value()
            stock_ticker_options = self.__get_stock_ticker_options(searcher_element, search_value)
            selected_stock_ticker = self.stock_ticker_selector_ui.get_selected_stock_ticker(stock_ticker_options)
            if selected_stock_ticker is not None:
                return selected_stock_ticker
