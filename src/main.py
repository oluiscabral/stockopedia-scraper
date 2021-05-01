'''
@author: oluiscabral
'''
from builders.simple_builder import SimpleBuilder
from scrapers.interfaces.scraper_component import ScraperComponent
from data_structure.data_ref import DataRef
from helpers.config import Config
from typing import Set
from data_structure.data import Data


def main(builder):
    # build application
    stock_ticker_selector = builder.stock_ticker_selector
    scraper: ScraperComponent = builder.scraper
    formatters = builder.formatters
    sender = builder.sender
    wd = builder.wd
    login_control = builder.login_control
    
    Config.initialize_defaults()
    # runs application
    try:
        while True:
            login_control.force_login()
            selected_stock_ticker = stock_ticker_selector.get_selected_stock_ticker()
            result:Set[Data] = scraper.scrap(wd, DataRef(selected_stock_ticker))
            for formatter in formatters:
                formatted_result = formatter.format(result)
                sender.send(formatted_result)
            print("All data has been succesfully sended to specified spreadsheet!")
    except Exception:
        wd.close()
        wd = None
        builder = None


if __name__ == '__main__':
    builder = SimpleBuilder()
    main(builder)
    
