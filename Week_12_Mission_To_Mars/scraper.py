from splinter import Browser as br
from bs4 import BeautifulSoup as bs
import requests as rq
import pandas as pd
import time

def initializeBrowser():
    executable_path ={'executable_path':'chromedriver.exe'}
    return br('chrome', **executable_path, headless=False)