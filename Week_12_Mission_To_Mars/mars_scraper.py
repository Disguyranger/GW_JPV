from splinter import Browser
from bs4 import BeautifulSoup as bs
import re, time

executable_path = {'executable_path': 'chromedriver.exe'}
browser = Browser('chrome', **executable_path)

def scraper():
    