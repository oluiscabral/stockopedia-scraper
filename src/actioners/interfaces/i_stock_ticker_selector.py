'''
@author: oluiscabral
'''
from abc import ABC, abstractmethod

class IStockTickerSelector(ABC):
    @abstractmethod
    def get_selected_stock_ticker(self)->str:
        pass