from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


driver =webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
cookie = driver.find_element(By.ID,"cookie")
items = driver.find_elements(By.CSS_SELECTOR,"#store b")
item_ids = [item.text for item in items]
item_prices = []

for price in items:
    element_text = price.text
    if element_text != "":
        cost = int(element_text.split("-")[1].strip().replace(",", ""))
        item_prices.append(cost)
print(item_prices)