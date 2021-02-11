from stockopedia_website import StockopediaWebsite
from scraped_data import MainScrapedData
from james_template import JamesTemplate
from config import Config
from google_spreadsheet import GoogleSpreadsheet
import tkinter as tk

Config.initialize_defaults()
stockopedia_website = StockopediaWebsite()

def scrap_func():
    global stock_ticker_var
    stock_ticker = stock_ticker_var.get()
    if len(stock_ticker.strip()) == 0:
        return None
    stockopedia_website.login(Config.get_email(), Config.get_password())
    main_webpage = stockopedia_website.get_main_webpage(stock_ticker)
    if main_webpage == None:
        print('Did not find a page for',stock_ticker,'stock ticker')
        return None
    scraped_data: MainScrapedData = main_webpage.scrap()
    formatted_datas = JamesTemplate.format(scraped_data)
    GoogleSpreadsheet.login()
    GoogleSpreadsheet.fill(formatted_datas)
    print('Data extraction completed!')

window = tk.Tk()
window.title('Stockopedia Scraper')
window.geometry('300x300')
window.anchor(tk.CENTER)

scrap_func = scrap_func

stock_ticker_label = tk.Label(text='stock ticker')
stock_ticker_label.grid(column=0, row=0)

stock_ticker_var = tk.StringVar()

stock_ticker_textbox = tk.Entry(width=20, textvariable=stock_ticker_var)
stock_ticker_textbox.grid(column=0, row=1)

scrap_button = tk.Button(text="Scrap", command=scrap_func)
scrap_button.grid(column=0, row=2)

window.mainloop()
