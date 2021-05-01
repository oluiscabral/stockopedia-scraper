'''
@author: oluiscabral
'''
from scrapers.url import URL
from actioners.interfaces.i_login_control import ILoginControl
from scrapers.composites.compare_scraper import CompareScraper
from creationals.stockreport_factory import StockReportScraperFactory
from creationals.compare_factory import CompareScraperFactory
from creationals.balance_factory import BalanceScraperFactory
from creationals.income_factory import IncomeScraperFactory
from creationals.cashflow_factory import CashflowScraperFactory
from scrapers.names import STOCKREPORT, COMPARE, BALANCE, INCOME, CASHFLOW

class ScraperFactory:
    @staticmethod
    def create_compare_scraper(login_control):
        compare_scraper = CompareScraper(COMPARE, URL('https://app.stockopedia.com/compare?tickers=${}'), login_control)
        compare_scraper.create_stockreport_scraper(ScraperFactory)
        return compare_scraper

    @staticmethod
    def create(t:str, login_control:ILoginControl):
        if t == STOCKREPORT:
            return StockReportScraperFactory.create(login_control)
        if t == COMPARE:
            return CompareScraperFactory.create(login_control)
        if t == BALANCE:
            return BalanceScraperFactory.create(login_control)
        if t == INCOME:
            return IncomeScraperFactory.create(login_control)
        if t == CASHFLOW:
            return CashflowScraperFactory.create(login_control)
        