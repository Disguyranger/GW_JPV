"""
Project 1: An Attempt at Reading The Stock Market
Team Name: -Pick Name-
    Members: John Vega, Patrick Huynh, Undraa Damdinsuren, Jawaher Abdulrahim
"""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import tkinter as tk
import requests, json
import datetime, time
from scipy.stats import linregress
#%%


coin_type = 'bitcoin'#input("What coin are you searching for: ").lower()
currency_type = 'usd'#input("What Currency type are you looking for: ")
time_frame = '31'#int(input("How far back would you like to look (in days format): "))

url = f'https://api.coingecko.com/api/v3/coins/{coin_type}/market_chart?vs_currency={currency_type}&days={time_frame}'
response = requests.get(url)
print(url)

data_construct = response.json()


date_time = []
value = []

for row in data_construct['prices']:
    date_time.append(datetime.datetime.utcfromtimestamp(row[0]/1000))
    value.append(row[1])
    
plt.figure(figsize=(9,5))
plt.xticks(rotation = 30)
plt.grid()
plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.plot(date_time, value, "-.", color = 'purple')
plt.title(f"Bitcoin price over {time_frame} days")
plt.xlabel('Date')
plt.ylabel('Price per Coin')



#%%