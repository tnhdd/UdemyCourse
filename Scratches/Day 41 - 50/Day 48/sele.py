from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.python.org/")

# price_euro = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
# print(f"The price is {price_euro.text}.{price_cents.text}")

driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul')

# time = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/time')
# name = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[3]/div[2]/div/ul/li[1]/a')

event_date = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_elements(By.CSS_SELECTOR, value=".event-widget li a")

events = {}

for n in range(len(event_date)):
    events[n] = {
        "time": event_date[n].text,
        "name": event_name[n].text,
    }
print(events)

driver.quit()
