'''
@author: oluiscabral
'''
from helpers.webdriver_factory import WebdriverFactory
from ui.login_ui import LoginUI
from actioners.login_control import LoginControl
from ui.stock_ticker_selector_ui import StockTickerSelectorUI
from scrapers.composites.base_composite import BaseComposite
from scrapers.names import *  # @NoMove @UnusedWildImport
from creationals.scraper_factory import ScraperFactory
from actioners.stock_ticker_selector import StockTickerSelector
from formatters.formatter import Formatter
from templates.template import Template
from senders.google_spreadsheet import GoogleSpreadsheet
from scrapers.workers.stock_ticker_worker import StockTickerWorker
from scrapers.workers.timestamp_worker import TimestampWorker


class SimpleBuilder:
    def create_stock_ticker_selector(self):
        stock_ticker_selector_ui = StockTickerSelectorUI()
        self.stock_ticker_selector = StockTickerSelector(self.wd, stock_ticker_selector_ui)

    def create_scraper(self):
        scraper = BaseComposite('main')
        stockreport_scraper = ScraperFactory.create(STOCKREPORT, self.login_control)
        compare_scraper = ScraperFactory.create(COMPARE, self.login_control)
        balance_scraper = ScraperFactory.create(BALANCE, self.login_control)
        income_scraper = ScraperFactory.create(INCOME, self.login_control)
        cashflow_scraper = ScraperFactory.create(CASHFLOW, self.login_control)
        scraper.add_children(StockTickerWorker(STOCK_TICKER))
        scraper.add_children(TimestampWorker(TIMESTAMP))
        scraper.add_children(stockreport_scraper)
        scraper.add_children(compare_scraper)
        scraper.add_children(balance_scraper)
        scraper.add_children(income_scraper)
        scraper.add_children(cashflow_scraper)
        self.scraper = scraper

    def __init__(self):
        self.wd = WebdriverFactory.create()
        self.login_control = LoginControl(self.wd, LoginUI())
        self.create_stock_ticker_selector()
        self.create_scraper()
        self.create_formatters()
        self.sender = GoogleSpreadsheet

    def create_formatters(self):
        self.formatters = set()
        self.formatters.add(self.create_stockreport_formatter())
        self.formatters.add(self.create_balance_formatter())
        self.formatters.add(self.create_income_formatter())
        self.formatters.add(self.create_cashflow_formatter())
        self.formatters.add(self.create_compare_formatter())

    def create_compare_formatter(self):
        compare_definition = {
            ('main', STOCK_TICKER): (0, 0),
            ('main', TIMESTAMP): (0, 1),
            ('main', COMPARE, COMPARE_TABLE): (1, 0)
        }
        compare_template = Template(compare_definition)
        return Formatter('S. Compare', 50, 20, compare_template)
    
    def create_cashflow_formatter(self):
        cashflow_definition = {
            ('main', STOCK_TICKER): (0, 0),
            ('main', TIMESTAMP): (0, 1),
            ('main', CASHFLOW, CASHFLOW_TABLE): (1, 0)
        }
        cashflow_template = Template(cashflow_definition)
        return Formatter('S. Cashflow', 50, 20, cashflow_template)

    def create_income_formatter(self):
        income_definition = {
            ('main', STOCK_TICKER): (0, 0),
            ('main', TIMESTAMP): (0, 1),
            ('main', INCOME, INCOME_TABLE): (1, 0)
        }
        income_template = Template(income_definition)
        return Formatter('S. Income Statement', 50, 20, income_template)

    def create_balance_formatter(self):
        balance_definition = {
            ('main', STOCK_TICKER): (0, 0),
            ('main', TIMESTAMP): (0, 1),
            ('main', BALANCE, BALANCE_TABLE): (1, 0)
        }
        balance_template = Template(balance_definition)
        return Formatter('S. Balance Sheet', 50, 20, balance_template)

    def create_stockreport_formatter(self):
        stockreport_definition = {
            ('main', STOCK_TICKER): (0, 0),
            ('main', TIMESTAMP): (0, 1),
            ('main', STOCKREPORT, STOCKREPORT_DESCRIPTION): (1, 0),
            ('main', STOCKREPORT, STOCKREPORT_MOMENTUM): (0, 5),
            ('main', STOCKREPORT, STOCKREPORT_RANKS): (0, 9),
            ('main', STOCKREPORT, STOCKREPORT_GV): (0, 12),
            ('main', STOCKREPORT, STOCKREPORT_ACTIVITY): (7, 0),
            ('main', STOCKREPORT, STOCKREPORT_SUMMARY): (12, 0),
            ('main', STOCKREPORT, STOCKREPORT_QUALITY): (13, 12),
            ('main', STOCKREPORT, STOCKREPORT_RATIOS): (24, 12),
            ('main', STOCKREPORT, STOCKREPORT_HISTORY): (34, 12),
            ('main', STOCKREPORT, STOCKREPORT_METER): (19, 12)
        }
        stockreport_template = Template(stockreport_definition)
        return Formatter('S. Stockreport', 50, 20, stockreport_template)
