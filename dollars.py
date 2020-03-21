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

root = Tk()
root.title('Valutaomvandlare 1.0')
root.geometry('400x150')

