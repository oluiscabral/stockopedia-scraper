'''
Created on Apr 29, 2021

@author: oluiscabral
'''
from scrapers.composites.compare_scraper import CompareScraper
from scrapers.names import COMPARE, COMPARE_TABLE
from scrapers.url import URL
from scrapers.workers.comparetable import CompareTable

class CompareScraperFactory:
    @staticmethod
    def create(login_control):
        compare_scraper = CompareScraper(COMPARE, URL('https://app.stockopedia.com/compare?tickers=${}'), login_control)
        compare_scraper.add_children(CompareTable(COMPARE_TABLE))
        return compare_scraper