'''
@author: oluiscabral
'''
from scrapers.composites.scraper_composite import ScraperComposite
from scrapers.url import URL
from scrapers.workers.singletable import SingleTable
from scrapers.names import INCOME, INCOME_TABLE

class IncomeScraperFactory:
    @staticmethod
    def create(login_control):
        income_scraper = ScraperComposite(INCOME, URL('https://app.stockopedia.com/share-prices/${}/income-statement'), login_control)
        income_scraper.add_children(SingleTable(INCOME_TABLE))
        return income_scraper