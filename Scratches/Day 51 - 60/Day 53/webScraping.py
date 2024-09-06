import time

from selenium import webdriver
from selenium.webdriver.common.by import By
import requests
from bs4 import BeautifulSoup

google_form = "https://forms.gle/srfQYKVsUkKDfzXX8"
url = "https://appbrewery.github.io/Zillow-Clone/"

response = requests.get(url)
data = response.text
soup = BeautifulSoup(data, "html.parser")

# Create a list of all the links on the page using a CSS Selector
all_link_elements = soup.select(".StyledPropertyCardDataWrapper a")
all_links = [link["href"] for link in all_link_elements]
print(all_links)

# Create a list of price per month
all_price_elements = soup.select(".PropertyCardWrapper span")
price_text = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements]
print(price_text)

# Create a list of address
all_address_elements = soup.select(".StyledPropertyCardDataWrapper address")
address_text = [address.get_text().strip() for address in all_address_elements]
print(address_text)

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)

for n in range(len(address_text)):
    driver.get(google_form)
    time.sleep(2)
    address = driver.find_element(By.XPATH,
                                  value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')

    price = driver.find_element(By.XPATH,
                                value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')

    link = driver.find_element(By.XPATH,
                               value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')

    submit = driver.find_element(By.XPATH,
                                 value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    address.send_keys(address_text[n])
    price.send_keys(price_text[n])
    link.send_keys(all_links[n])
    submit.click()
