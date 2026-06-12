import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Твой логин GitHub уже вставлен
GITHUB_USERNAME = "DecodeEynSof"
BASE_URL = f"https://{GITHUB_USERNAME}.github.io/music-studio/"

@pytest.fixture
def driver():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.implicitly_wait(5)
    yield driver
    driver.quit()

def test_main_page_opens(driver):
    driver.get(BASE_URL)
    assert "Музыкальная студия" in driver.title

def test_biography_link(driver):
    driver.get(BASE_URL)
    link = driver.find_element(By.LINK_TEXT, "Биография Марии Алексеевны Семьянской")
    link.click()
    assert "Биография" in driver.title

def test_history_link(driver):
    driver.get(BASE_URL)
    link = driver.find_element(By.LINK_TEXT, "История создания музыкальной школы")
    link.click()
    assert "История школы" in driver.title

def test_svoya_versia_link(driver):
    driver.get(BASE_URL)
    link = driver.find_element(By.LINK_TEXT, "Уникальная учебная программа \"Своя версия\"")
    link.click()
    assert "Своя версия" in driver.title

def test_clubs_link(driver):
    driver.get(BASE_URL)
    link = driver.find_element(By.LINK_TEXT, "Направления школы")
    link.click()
    WebDriverWait(driver, 5).until(EC.url_contains("/clubs/"))
    assert "/clubs/" in driver.current_url

def test_creative_workshop_link(driver):
    driver.get(BASE_URL)
    link = driver.find_element(By.LINK_TEXT, "Творческая мастерская")
    link.click()
    WebDriverWait(driver, 5).until(EC.url_contains("/creative-workshop/"))
    assert "/creative-workshop/" in driver.current_url

def test_rent_link(driver):
    driver.get(BASE_URL)
    link = driver.find_element(By.LINK_TEXT, "Аренда помещения и оборудования")
    link.click()
    assert "Аренда" in driver.title

def test_contacts_link(driver):
    driver.get(BASE_URL)
    link = driver.find_element(By.LINK_TEXT, "Адрес и контакты")
    link.click()
    assert "Контакты" in driver.title
