from tkinter import *
from tkinter import ttk
import requests
from bs4 import BeautifulSoup

def kursScrape():
    global dollarKurs
    url = requests.get('https://www.di.se/valutor/usdsek-26491/').text
    soup = BeautifulSoup(url, 'html.parser')

    data = soup.find('span', {'class': 'js_real-time-stock-details-price'}).text

    dollarKurs = float(data.replace(',', '.'))

    return dollarKurs
kursScrape()
def count():
    getSek = entry.get()
    getSek = float(getSek)

    try:
        exchange = round(getSek / dollarKurs, 2)
        info['text'] = f'Du får {exchange} dollar!'
    except:
        print('Funkar inte')



#TODO Bättre layout!
root = Tk()
root.title('Valutaomvandlare 1.0')
root.geometry('245x147')


head = Label(root, text='Valutaomvandlare')
head.grid(row=0, column=1)
head1 = Label(root, text='Sek till Dollar')
head1.grid(row=1, column=1)

ange = Label(root, text='Ange sek:')
ange.grid(sticky=E)

entry = Entry(root)
entry.grid(row=2, column=1, padx=5)


btn1 = ttk.Button(root, text='Växla', command=count)
btn1.grid(row=4, column=1, pady=20, padx=5)

info = Label(root)
info.grid(row=3, column=1)

root.mainloop()
