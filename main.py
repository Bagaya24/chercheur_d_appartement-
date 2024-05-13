import time

import requests
from selenium import webdriver
from bs4 import BeautifulSoup
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(r"C:\Users\bagay\OneDrive\Documents\Udemy\chromedriver-win64\chromedriver.exe",
                          options=chrome_options)

response = requests.get(url="https://appbrewery.github.io/Zillow-Clone/")
response.raise_for_status()

web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

web_prices = soup.select("div div .PropertyCardWrapper__StyledPriceLine")
all_prices = [price.string.replace("$", "").replace("+", "").replace("/mo", "").split()[0] for price in web_prices]

web_address = soup.select("div div a address")
all_address = [web_address.string.replace("\n", "").strip() for web_address in web_address]

web_link = soup.select("div .StyledPropertyCardDataWrapper a")
all_links = [link.get("href") for link in web_link]


driver.get(url="https://docs.google.com/forms/d/e/1FAIpQLSdULhwGYa8Ku-AXQRjsxxx_UOCExqFQXWJGMn3VdWZ6ZYRJTQ/viewform?usp=sf_link")
for i in range(len(all_prices)):

    time.sleep(3)
    inputs = driver.find_elements(By.CSS_SELECTOR, value='.geS5n .oJeWuf .Xb9hP .zHQkBf')
    input_price = inputs[0]
    input_address = inputs[1]
    input_link = inputs[2]
    btn_send = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')

    time.sleep(5)

    input_price.send_keys(all_prices[i])
    input_address.send_keys(all_address[i])
    input_link.send_keys(all_links[i])
    btn_send.click()
    time.sleep(3)
    link_send_again = driver.find_element(By.LINK_TEXT, value="Envoyer une autre réponse")
    link_send_again.click()

    if i == 43:
        driver.quit()
