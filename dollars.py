from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def kursScrape():

    url = requests.get('https://www.di.se/valutor/usdsek-26491/').text
    soup = BeautifulSoup(url, 'html.parser')

    data = soup.find('span', {'class': 'js_real-time-stock-details-price'}).text

    dk = float(data.replace(',', '.'))

    print(dk)
#TODO Bättre layout!
root = Tk()
root.title('Valutaomvandlare 1.0')
root.geometry('250x100')

ram = Frame(bd=0, relief=FLAT)
ram.grid(row=0, column=0, pady=5, padx=5)

sek = Label(ram, text='Ange sek:')
sek.grid(row=0, column=0, sticky=W)
sek.entry = Entry(ram)
sek.entry.grid(row=0, column=1)

btn1 = ttk.Button(root, text='Växla')
btn1.grid(row=1, column=1, sticky=S)
root.mainloop()
