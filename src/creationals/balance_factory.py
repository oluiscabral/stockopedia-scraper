'''
@author: oluiscabral
'''
from scrapers.names import BALANCE, BALANCE_TABLE
from scrapers.composites.scraper_composite import ScraperComposite
from scrapers.url import URL
from scrapers.workers.singletable import SingleTable

class BalanceScraperFactory:
    @staticmethod
    def create(login_control):
        balance_scraper = ScraperComposite(BALANCE, URL('https://app.stockopedia.com/share-prices/${}/balance-sheet'), login_control)
        balance_scraper.add_children(SingleTable(BALANCE_TABLE))
        return balance_scraper