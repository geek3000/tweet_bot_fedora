from selenium import webdriver

import requests
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET
import time

def get_article():
    feed="https://fedoramagazine.org/"
    
    driver.get(feed)
    source=driver.page_source
    page = BeautifulSoup(source, 'html.parser')
    #get the information about first article
    h2=page.find("h2", {"class", "post-title"})
    link=h2.find("a")
    title=link.text
    post_link=link.get("href")
    print(title, post_link)
    return [title, post_link]
    
def post_tweet(title, url):
    
    driver.get("https://twitter.com/login")
    
    login_field = driver.find_element_by_class_name("js-username-field")
    login_field.clear()

    # enter username
    login_field.send_keys("")

    password_field = driver.find_element_by_class_name("js-password-field")
    password_field.clear()

    #enter password
    password_field.send_keys("")

    password_field.submit()
    time.sleep(6)
    tweet_box=driver.find_element_by_css_selector("div[role='textbox']")
    tweet_box.clear()
    tweet_box.send_keys(title+"  "+url)

    tweet_btn=driver.find_elements_by_css_selector("div[data-testid='tweetButtonInline']")
    for elt in tweet_btn:
        elt.click()
driver = webdriver.Chrome()
info=get_article()
post_tweet(info[0], info[1])
