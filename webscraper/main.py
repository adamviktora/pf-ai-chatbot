import json

from selenium import webdriver
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

components = {}

for href in hrefs:
    if "all-components" in href:
        continue
    driver.get(href)
    name = driver.find_element(By.ID, "ws-page-title").text
    div_elem = driver.find_element(By.CSS_SELECTOR, "div.pf-v5-c-page__main-group")
    description = div_elem.find_element(By.TAG_NAME, "p").text
    components[name.lower()] = {"name": name, "link": href, "description": description}

driver.quit()

# Specify the file path
file_path = "../chatbot/actions/components.json"

# Save the data as JSON
with open(file_path, "w") as json_file:
    json.dump(components, json_file)

print(f"Components details were saved to {file_path}")
