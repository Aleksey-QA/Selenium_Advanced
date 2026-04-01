import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--window-size=1980,1080")
driver = webdriver.Chrome(options=options)

FOR_BUSINESS_BUTTON_LOCATOR = ("xpath", "//a[text()=' For Business ']")
START_FREE_BUTTON_LOCATOR = ("xpath", "//a[@class='button-nav w-inline-block']")

driver.get("https://hyperskill.org/tracks")

driver.find_element(*FOR_BUSINESS_BUTTON_LOCATOR).click()
time.sleep(1)

tabs = driver.window_handles#вносит все окна в список
driver.switch_to.window(tabs[1])#переключение между окнами
driver.find_element(*START_FREE_BUTTON_LOCATOR).click()

tabs = driver.window_handles#вносит все окна в список
driver.switch_to.window(tabs[0])
time.sleep(1)
driver.switch_to.window(tabs[1])
time.sleep(1)
driver.switch_to.window(tabs[2])
time.sleep(1)
driver.switch_to.window(tabs[0])
time.sleep(1)
print(driver.window_handles)
driver.quit()  # Закрывает все окна и завершает сессию
