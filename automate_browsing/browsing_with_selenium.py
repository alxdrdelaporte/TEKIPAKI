#!/usr/lib/python3.8
# -*-coding:utf-8 -*
"""
Alexander DELAPORTE - CRLAO
https://tekipaki.hypotheses.org/
https://github.com/alxdrdelaporte/
https://gitlab.com/alxdrdelaporte

Navigate around a website with selenium library
INPUT
My Github page URL (https://alxdrdelaporte.github.io/)
OUTPUT
Console outputs
"""

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

options = webdriver.FirefoxOptions()
options.headless = True
webdrivers_path = "./WebDrivers/"
driver = webdriver.Firefox(webdrivers_path, options=options)


def enter_konamicode(url):
    """Go to URL, input Konami Code and return text from 'konamicongrats' element
    Parameter = page URL
    Works well with https://alxdrdelaporte.github.io/ (has 'konamicongrats' element)"""
    driver.get(url)
    body = driver.find_element_by_tag_name("body")
    # https://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.keys
    konamicode = [Keys.ARROW_UP, Keys.ARROW_UP,
                  Keys.ARROW_DOWN, Keys.ARROW_DOWN,
                  Keys.ARROW_LEFT, Keys.ARROW_RIGHT,
                  Keys.ARROW_LEFT, Keys.ARROW_RIGHT,
                  "b", "a"]
    body.send_keys(konamicode)
    time.sleep(1)
    konamialert = driver.find_element_by_id("konamicongrats")
    message = konamialert.text
    return message


def go_to_tekipaki(url):
    """
    Click on first link with "px-2.fa-lg.text-dark" class, return confirmation message
    Parameter = URL
    Works with https://alxdrdelaporte.github.io/ (link to https://tekipaki.hypotheses.org/)
    """
    driver.get(url)
    link = driver.find_element_by_class_name("px-2.fa-lg.text-dark")
    link.click()
    time.sleep(1)
    tekipaki = driver.current_url
    driver.get(tekipaki)
    titre = driver.find_element_by_class_name("site-title").text
    description = driver.find_element_by_class_name("site-description").text
    message = f"""
Bravo, vous êtes bien sur {titre} !
{tekipaki}
{description}"""
    return message


page = 'https://alxdrdelaporte.github.io/'
print(enter_konamicode(page))
print(go_to_tekipaki(page))
