from template import Template
import typing
from scraped_data import MainScrapedData
from bs4 import BeautifulStoneSoup
from formatted_data import FormattedData
from config import Config
from selenium.webdriver.remote.webelement import WebElement

class JamesTemplate(Template):
    @staticmethod
    def format(scraped_data:MainScrapedData) -> typing.List[FormattedData]:
        ret: typing.List[FormattedData] = []
        ret.append(JamesTemplate.get_main(scraped_data.main))
        compare = scraped_data.compare
        if len(compare):
            ret.append(JamesTemplate.get_compare(compare))
        return ret
        
    @staticmethod
    def get_main(main_data) -> FormattedData:
        main:typing.List[typing.List[str]] = [[' ' for i in range(16)] for j in range(50)]  # @UnusedVariable
        main[0][0] = main_data['url']
        main[0][1] = str(main_data['time-stamp'])
        main[1][0] = main_data['name']
        JamesTemplate.add_desc(2, 0, main_data['desc'], main)
        JamesTemplate.add_momentum(1, 5, main_data['momentum'][0], main)
        JamesTemplate.add_ranks(2, 9, main_data['ranks'], main)
        JamesTemplate.add_gv(1,12, main_data['gv'][0], main)
        JamesTemplate.add_gv(14,12, main_data['quality'], main)
        JamesTemplate.add_summary(13,0, main_data['summary'][0], main)
        JamesTemplate.add_meter(20, 12, main_data['meters'], main)
        JamesTemplate.add_other_ratios(25, 12, main_data['other-ratios'][0], main)
        JamesTemplate.add_momentum(35, 12, main_data['recent-story'], main)
        return FormattedData(Config.get_main_sheet_name(), main)
    
    @staticmethod
    def add_to_list(l,c, content:str, ls):
        content = content.strip()
        if len(content) != 0:
            ls[l][c] = content
    
    @staticmethod
    def add_element_to_list(l,c, element:WebElement, ls):
        if element != None:
            content = element.text.strip()
            if len(content) != 0:
                ls[l][c] = content
        
    
    @staticmethod
    def get_compare(compare_data) -> FormattedData:
        compare:typing.List[typing.List[str]] = [[' ' for i in range(100)] for j in range(60)]  # @UnusedVariable
        compare[0][0] = compare_data['url']
        compare[0][1] = str(compare_data['time-stamp'])
        JamesTemplate.add_stock_tickers(1, 1, compare_data['stock-tickers'], compare)
        JamesTemplate.add_tbody(2, 0, compare_data['tbody'], compare)
        return FormattedData(Config.get_compare_sheet_name(), compare)
    
    @staticmethod
    def add_stock_tickers(l, c, stock_tickers, compare):
        for i, stock_ticker in enumerate(stock_tickers):
            JamesTemplate.add_to_list(l, c+i, stock_ticker, compare)
    
    @staticmethod
    def add_tbody(l, c, tbody, compare):
        for tr in tbody.find_all('tr'):
            for j, td in enumerate(tr.find_all('td')):
                JamesTemplate.add_element_to_list(l, c+j, td, compare)
            l+=1
        
        
    @staticmethod
    def add_desc(l, c, desc, main):
        for i, element in enumerate(desc):
            children = list(element.children)
            JamesTemplate.add_element_to_list(l+i, c, children[0], main)
            JamesTemplate.add_element_to_list(l+i, c+1, children[1], main)
    
    @staticmethod
    def add_momentum(l, c, momentum:BeautifulStoneSoup, main):
        title:BeautifulStoneSoup = momentum.findChild('h5')
        JamesTemplate.add_element_to_list(l, c, title, main)
        tables = momentum.find_all('table')
        for table in tables:
            l += 1
            table:BeautifulStoneSoup
            thead:BeautifulStoneSoup = table.find('thead')
            JamesTemplate.add_element_to_list(l, c, thead, main)
            tbody = table.find('tbody')
            for tr in tbody.find_all('tr'):
                l += 1
                tr:BeautifulStoneSoup
                tds = tr.find_all('td')
                for i, td in enumerate(tds):
                    JamesTemplate.add_element_to_list(l, c+i, td, main)
    
    @staticmethod
    def add_gv(l, c, gv:BeautifulStoneSoup, main):
        title:BeautifulStoneSoup = gv.findChild('h5')
        JamesTemplate.add_element_to_list(l, c, title, main)
        tables = gv.find_all('table')
        for table in tables:
            l += 1
            table:BeautifulStoneSoup
            thead:BeautifulStoneSoup = table.find('thead')
            for i,th in enumerate(thead.select('th')):
                JamesTemplate.add_element_to_list(l, c+i, th, main)
            tbody = table.find('tbody')
            for tr in tbody.find_all('tr'):
                l += 1
                tr:BeautifulStoneSoup
                divs = tr.find('td').find('div').find_all('div')
                values = [e.text.strip() for e in divs]
                JamesTemplate.add_to_list(l, c, values[0], main)
                JamesTemplate.add_to_list(l, c+1, values[1], main)
    
    @staticmethod
    def add_ranks(l, c, ranks, main):
        for rank in ranks:
            rank:BeautifulStoneSoup
            divs = rank.find_all('div')
            title = divs[0]
            JamesTemplate.add_element_to_list(l, c, title, main)
            value = divs[1].find('span').find_all('span')[1]
            JamesTemplate.add_element_to_list(l, c+1, value, main)
            l += 1
            
    @staticmethod
    def add_summary(l, c, summary, main):
        title:BeautifulStoneSoup = summary.findChild('h5')
        JamesTemplate.add_element_to_list(l, c, title, main)
        table:BeautifulStoneSoup = summary.select('table')[1]
        thead:BeautifulStoneSoup = table.find('thead')
        l+=1
        for i, th in enumerate(thead.find_all('th')):
            JamesTemplate.add_element_to_list(l, c+i, th, main)
        tbody = table.find('tbody')
        for tr in tbody.find_all('tr'):
            tds = tr.find_all('td')
            if len(tds) == 0:
                continue
            l += 1
            tr:BeautifulStoneSoup
            for i, td in enumerate(tds):
                JamesTemplate.add_element_to_list(l, c+i, td, main)
    
    @staticmethod
    def add_meter(l, c, meters, main):
        length = len(meters)
        labels = []
        values = []
        for meter in meters:
            meter:BeautifulStoneSoup
            main_div = meter.find('div').find('div')
            divs = main_div.find_all('div')
            labels.append(divs[0].text.strip())
            values.append(divs[1].text.strip())
        for i in range(length):
            JamesTemplate.add_to_list(l+i, c, labels[i], main)
            JamesTemplate.add_to_list(l+i, c+1, values[i], main)
    
    @staticmethod
    def add_other_ratios(l, c, other_ratios, main):
        title:BeautifulStoneSoup = other_ratios.findChild('h5')
        JamesTemplate.add_element_to_list(l, c, title, main)
        tables:BeautifulStoneSoup = other_ratios.select('table')
        for table in tables:
            l+=1
            thead:BeautifulStoneSoup = table.find('thead')
            for i, th in enumerate(thead.select('th')):
                JamesTemplate.add_element_to_list(l, c+i, th, main)
            tbody = table.find('tbody')
            for tr in tbody.find_all('tr'):
                l += 1
                tr:BeautifulStoneSoup
                tds = tr.find_all('td')
                for i, td in enumerate(tds):
                    JamesTemplate.add_element_to_list(l, c+i, td, main)
    
    
        
        
        
        