from bs4 import BeautifulSoup as bsp
from splinter import Browser as br
import pandas as pd
import requests as rq
import time, numpy

def init_browser():
    executable_path = {'executable_path': 'chromedriver.exe'} #Executable Path
    return bsp('chrome', **executable_path, headless=False)

def scrape():
    browser = init_browser()
    scrape_mars_list = []
    html = browser.html
    
    mars_news_url = 'https://mars.nasa.gov/news/?page=0&per_page=40&order=publish_date+desc%2Ccreated_at+desc&search=&category=19%2C165%2C184%2C204&blank_scope=Latest'
    response = rq.get(mars_news_url)
    soup = bsp(response.text, 'html.parser')
    pulled_html_results = soup.find_all('div', class_='rollover_description_inner')
    pulled_html_title_results = soup.find_all('div', class_='content_title')
    print(pulled_html_results, pulled_html_title_results)
    pulled_title = pulled_html_results[0].text.strip()
    pulled_paragraph = pulled_html_title_results[0].text.strip()

    image_url = 'https://www.jpl.nasa.gov/spaceimages/?search=&category=Mars'
    browser.visit(image_url)
    time.sleep(1)
    soup = bsp(html, 'html.parser')
    result = soup.find('div', class_='img')
    featured_image_url = result.img['src']

    weather_twitter_url = 'https://twitter.com/marswxreport?lang=en'
    browser.visit(weather_twitter_url)
    time.sleep(1)
    soup = bsp(html, 'html.parser')
    result = soup.find_all('span', class_='css-901oao css-16my406 r-1qd0xha r-ad9z0 r-bcqeeo r-qvutc0')
    mars_weather = result[27].text
    

    facts_url = 'https://space-facts.com/mars/'
    tables = pd.read_html(facts_url)
    mars_facts_df = tables[2]
    mars_facts_df = mars_facts_df.rename(columns = {0: 'Description', 1: Fact})
    mars_facts_df.set_index('Description', inplace = True)
    mars_facts_html_table = marts_facts_df.to_html()
    mars_facts_html_table.replace('\n', '')
    mars_facts_df.to_html('mars_facts_table.html')

    hemi_list = ['Cereberus', 'Schiaparelli', 'Syrtis', 'Valles']
    hemi_img_urls = []

    hemi_url = 'https://astrogeology.usgs.gov/search/results?q=hemisphere+enhanced&k1=target&v1=Mars'
    browser.visit(hemi_url)
    time.sleep(1)

    for x in hemi_list:
        browser.links.find_by_partial_text(x).click()
        browser.find_link_by_text('Open').first.click()
        soup = bsp(html, 'html.parser')
        img_url = soup.find('img', class_='wide-image')['src']
        title = soup.find('h2', class_='title').text
        hemi_img_urls.append({'title':title, 'img_url': img_url})

    record = {
        'title': pulled_title,
        'paragraph': pulled_paragraph,
        'image': featured_image_url,
        'hemi_image': hemi_img_urls
    }
    scrape_mars_list.append(record)

    return scrape_mars_list
    

