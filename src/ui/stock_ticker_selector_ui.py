'''
@author: oluiscabral
'''
from ui.interfaces.i_stock_ticker_selector_ui import IStockTickerSelectorUI

class StockTickerSelectorUI(IStockTickerSelectorUI):
    def get_search_value(self)->str:
        print("Insert what stock ticker you want to search.")
        return input("search: ")

    def __get_stock_ticker_options_dict(self, stock_ticker_options):
        stock_ticker_options_dict = {i + 1: stock_ticker_option for i, stock_ticker_option in enumerate(stock_ticker_options)}
        stock_ticker_options_dict[0] = "None of these options."
        return stock_ticker_options_dict

    def __print_stock_ticker_options_dict_items(self, stock_ticker_options_dict_items):
        for stock_ticker_options_dict_key, stock_ticker_options_dict_value in stock_ticker_options_dict_items:
            print(stock_ticker_options_dict_key, '.', stock_ticker_options_dict_value)

    def __print_stock_ticker_selection_enunciation(self, stock_ticker_options_dict_items):
        print("Stock ticker options: ")
        self.__print_stock_ticker_options_dict_items(stock_ticker_options_dict_items)
        print("Select one of these options (number).")

    def __get_selected_stock_ticker_option(self, stock_ticker_options_dict):
            selected_stock_ticker_option_key = int(input("selection: "))
            if selected_stock_ticker_option_key in stock_ticker_options_dict:
                if selected_stock_ticker_option_key == 0:
                    return None
                return stock_ticker_options_dict[selected_stock_ticker_option_key]
            raise Exception()
            
    def get_selected_stock_ticker(self, stock_ticker_options)->str:
        stock_ticker_options_dict = self.__get_stock_ticker_options_dict(stock_ticker_options)
        stock_ticker_options_dict_items = stock_ticker_options_dict.items()
        while True:
            self.__print_stock_ticker_selection_enunciation(stock_ticker_options_dict_items)
            try:
                return self.__get_selected_stock_ticker_option(stock_ticker_options_dict)
            except Exception:
                print("-"*50)
                print("Invalid selection.")
                print("Try again.")
                print("-"*50)
        
        
        
        
            