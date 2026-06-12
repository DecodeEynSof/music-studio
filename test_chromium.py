from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service("/usr/bin/chromedriver")
options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/chromium-browser"

driver = webdriver.Chrome(service=service, options=options)
driver.get("https://google.com")
print(driver.title)
driver.quit()
