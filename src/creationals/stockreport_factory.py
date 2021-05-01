'''
@author: oluiscabral
'''
from scrapers.composites.scraper_composite import ScraperComposite
from scrapers.url import URL
from scrapers.workers.stockreport_activity import StockReportActivity
from scrapers.workers.stockreport_description import StockReportDescription
from scrapers.workers.stockreport_gv import StockReportGV
from scrapers.workers.stockreport_history import StockReportHistory
from scrapers.workers.stockreport_meter import StockReportMeter
from scrapers.workers.stockreport_momentum import StockReportMomentum
from scrapers.workers.stockreport_quality import StockReportQuality
from scrapers.workers.stockreport_ranks import StockReportRanks
from scrapers.workers.stockreport_ratios import StockReportRatios
from scrapers.workers.stockreport_similar import StockReportSimilar
from scrapers.workers.stockreport_summary import StockReportSummary
from scrapers.names import *  # @UnusedWildImport

class StockReportScraperFactory:
    @staticmethod
    def create(login_control):
        stockreport_scraper = ScraperComposite(STOCKREPORT, URL('https://app.stockopedia.com/share-prices/${}'), login_control)
        stockreport_scraper.add_children(StockReportActivity(STOCKREPORT_ACTIVITY))
        stockreport_scraper.add_children(StockReportDescription(STOCKREPORT_DESCRIPTION))
        stockreport_scraper.add_children(StockReportGV(STOCKREPORT_GV))
        stockreport_scraper.add_children(StockReportHistory(STOCKREPORT_HISTORY))
        stockreport_scraper.add_children(StockReportMeter(STOCKREPORT_METER))
        stockreport_scraper.add_children(StockReportMomentum(STOCKREPORT_MOMENTUM))
        stockreport_scraper.add_children(StockReportQuality(STOCKREPORT_QUALITY))
        stockreport_scraper.add_children(StockReportRanks(STOCKREPORT_RANKS))
        stockreport_scraper.add_children(StockReportRatios(STOCKREPORT_RATIOS))
        stockreport_scraper.add_children(StockReportSimilar(STOCKREPORT_SIMILAR))
        stockreport_scraper.add_children(StockReportSummary(STOCKREPORT_SUMMARY))
        return stockreport_scraper


