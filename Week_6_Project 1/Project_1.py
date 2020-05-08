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
import sys
def storyPrint(text):
    for letter in text:
        sys.stdout.write(letter)
        sys.stdout.flush()
        time.sleep(.04)
    print("\n")
    
    
def dataFrameCreation(coin_type, currency_type, time_frame):
    date_time = []
    value = []
    
    url = f'https://api.coingecko.com/api/v3/coins/{coin_type}/market_chart?vs_currency={currency_type}&days={time_frame}'
    response = requests.get(url)
    data_construction = response.json()
    if data_construction == {"error":"Could not find coin with the given id"}:
        fail = (f"You goofed.\nThe Cryptocoin: {coin_type} doesn't exist. \nPlease try again with the correct parameters.")
        storyPrint(fail)
    elif data_construction == {'error': 'invalid vs_currency'}:
        fail = (f"You goofed.\nThe Currency type: {currency_type} doesn't exist. \nPlease try again with the correct parameters.")
        storyPrint(fail)
    else:
        for row in data_construction['prices']:
            date_time.append(datetime.datetime.utcfromtimestamp(row[0]/1000))
            value.append(row[1])
    
    return(date_time, value)

def dataFrameBaby(date_time, value):
    date_time = date_time.split(' ')
    date = date_time[0]
    time = date_time[1]
    print(date, time)

def main():
    quickKeys = {'1': 'bitcoin', '2': 'litecoin', '3': 'ethereum'}
    coin_type = input("""What coin are you searching for? \n Here is a quick list in case you find yourself in a bind --[1] for Bitcoin (BTC), [2] for Litecoin (LTC), [3] Ethereum (ETH): """).lower()
    if coin_type == '1' or coin_type == "2" or coin_type == '3':
        coin_type = quickKeys[coin_type]
    currency_type = input('What currency type are you looking for: ').lower()
    
    while True:
        try:
            time_frame = int(input("How far back would you like to look (in days format): "))
            break
        except ValueError:
            print('Value is not an integer. Please, try again.')
        

    notFail = (f"You are looking for {coin_type.capitalize()}'s price, in {currency_type.upper()} in a time frame of {time_frame} days")
    storyPrint(notFail)
    date_time, value = dataFrameCreation(coin_type, currency_type, time_frame)
    dataFrameBaby(date_time, value)



main()