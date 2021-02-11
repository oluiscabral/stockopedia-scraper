import tkinter as tk


class MainPage(object):
    def __init__(self):
        window = tk.Tk()
        window.title('Stockopedia Scraper')
        window.geometry('600x400')
        window.anchor(tk.CENTER)

        stock_ticker_label = tk.Label(text='stock ticker')
        stock_ticker_label.grid(column=0, row=0)

        self.stock_ticker = tk.StringVar()

        stock_ticker_textbox = tk.Entry(width=20, textvariable=self.stock_ticker)
        stock_ticker_textbox.grid(column=0, row=1)

        scrap_button = tk.Button(text="Scrap", command=MainPage.scrap)
        scrap_button.grid(column=0, row=2)

        window.mainloop()
