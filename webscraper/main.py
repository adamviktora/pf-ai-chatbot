from pprint import pprint

from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options

domain = "http://localhost:8003"

# Configure Firefox options
options = Options()
options.add_argument("-headless")

# Instantiate the Firefox WebDriver with options
driver = webdriver.Firefox(options=options)

# Navigate to Url
driver.get(domain)

list_items = driver.find_elements(By.CSS_SELECTOR, "li.ws-side-nav-group")
goal_li = []

for li in list_items:
    button = li.find_element(By.TAG_NAME, "button")
    if button.text == "Components":
        goal_li.append(li)

elements = goal_li[0].find_elements(By.TAG_NAME, "a")
hrefs = [element.get_attribute("href") for element in elements]

components = []

for href in hrefs:
    driver.get(href)
    name = driver.find_element(By.ID, "ws-page-title").text
    div_elem = driver.find_element(By.CSS_SELECTOR, "div.pf-v5-c-page__main-group")
    try:
        description = div_elem.find_element(By.TAG_NAME, "p").text
    except NoSuchElementException:
        description = ""

    components.append({"name": name, "link": href, "description": description})

driver.quit()

pprint(components)
