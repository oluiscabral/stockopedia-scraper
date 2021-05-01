'''
@author: oluiscabral
'''
from abc import ABC, abstractmethod

class IStockTickerSelectorUI(ABC):
    @abstractmethod
    def get_search_value(self)->str:
        pass
    @abstractmethod
    def get_selected_stock_ticker(self, stock_ticker_options)->str:
        pass