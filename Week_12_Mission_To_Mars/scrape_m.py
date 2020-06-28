from splinter import Browser
from bs4 import BeautifulSoup as bs
import requests, time
import pandas as pd


def init_browser():
    executable_path = {"executable_path": "chromedriver.exe"} # WINDOWS USERS!
    return Browser("chrome", **executable_path, headless=False)

def scrape():
    browser = init_browser()
    marsScrape = []
    url = "https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest"
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    paragraphResults = soup.find_all('div', class_='rollover_description_inner')
    titleResults = soup.find_all('div', class_='content_title')
    newsTitle = titleResults[0].text.strip()
    newsParagraph = paragraphResults[0].text.strip()

    imageUrl = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(imageUrl)
    time.sleep(3)
    html = browser.html
    soup = bs(html, 'html.parser')
    result = soup.find('div', class_='img')
    featured_image_url = result.img['src']

    weatherUrl = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weatherUrl)
    time.sleep(3)
    tw_html = browser.html
    soup = bs(html, 'html.parser')
    result = soup.find('div', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0x r-bcqeeo r-qvutc0')
    featured_image_url = tw_html[27].text

    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    marsFactsDF = tables[2]
    marsFactsDF = marsFactsDF.rename(columns = {0:'Description', 1: 'Facts'})
    marsFactsDF.set_index('Description', inplace = True)
    marsFactsHTML = marsFactsDF.to_html()
    marsFactsHTML.replace('\n','')
    marsFactsDF.to_html('FactsAboutMars.html')

    hemList = ['Cerberus', 'Schiaparelli', 'Syrtis', 'Valles']
    hemListUrl = []
    hemUrl = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&' #FINISH
    browser.visit(hemUrl)
    time.sleep(3)
    for x in hemList:
        browser.links.find_by_partial_text(x).click()
        browser.find_link_by_text('Open').first.click()
        html = browser.html
        soup = bs(html, 'html.parser')
        img_url = soup.find('img', class_='wide-image')['src']
        title = soup.find('h2', class_='title')
        hemListUrl.append({'title':title, 'img_url':img_url})

    record = {'title': newsTitle,
     'paragraph': newsParagraph, 
     'image': featured_image_url,
      'hemi_image': hemListUrl
    }
    marsScrape.append(record)

    