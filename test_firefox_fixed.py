from selenium import webdriver
from selenium.webdriver.firefox.service import Service

service = Service('/usr/local/bin/geckodriver')
driver = webdriver.Firefox(service=service)

driver.get("https://google.com")
print("Заголовок:", driver.title)
driver.quit()
