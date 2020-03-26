from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup



class Exchange:

    def __init__(self, master):
        self.master = master
        master.title('Valutaomvandlare 1.5')
        master.geometry('254x147')

        self.head1 = Label(root, text='Valutaomvandlare')
        self.head1.grid(row=0, column=1)

        self.head2 = Label(root, text='SEK --> Dollar')
        self.head2.grid(row=1, column=1)

        self.sek = Label(root, text='Ange Sek:')
        self.sek.grid(sticky=E)

        self.entry = Entry(root)
        self.entry.grid(row=2, column=1, padx=5)
        self.entry.bind('<Return>', self.count)

        self.btn1 = ttk.Button(root, text='Växla', command=self.count)
        self.btn1.grid(row=4, column=1, pady=20, padx=5)

        self.info = Label(root)
        self.info.grid(row=3, column=1)



    def exchangeRate(self):
        url = requests.get('https://www.di.se/valutor/usdsek-26491/').text
        soup = BeautifulSoup(url, 'html.parser')

        data = soup.find('span', {'class': 'js_real-time-stock-details-price'}).text

        dollarKurs = float(data.replace(',', '.'))

        return dollarKurs

    def count(self, *args):
        getSek = self.entry.get()
        try:
            getSek = float(getSek)
            exchange = round(getSek / self.exchangeRate(), 3)
            self.info['text'] = f'Du får {exchange} dollar.'
        except:
            self.info['text'] = 'Fel, Försök igen!'



root = Tk()
app = Exchange(root)
root.mainloop()
