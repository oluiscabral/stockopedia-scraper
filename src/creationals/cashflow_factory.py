'''
@author: oluiscabral
'''
from scrapers.names import CASHFLOW, CASHFLOW_TABLE
from scrapers.composites.scraper_composite import ScraperComposite
from scrapers.url import URL
from scrapers.workers.singletable import SingleTable

class CashflowScraperFactory:
    @staticmethod
    def create(login_control):
        cashflow_scraper = ScraperComposite(CASHFLOW, URL('https://app.stockopedia.com/share-prices/${}/cashflow'), login_control)
        cashflow_scraper.add_children(SingleTable(CASHFLOW_TABLE))
        return cashflow_scraper