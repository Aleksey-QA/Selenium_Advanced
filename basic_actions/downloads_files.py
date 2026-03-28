import os
import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": f"{os.getcwd()}\downloads"
}
print(prefs)
chrome_options.add_experimental_option("prefs", prefs)
#chrome_options.add_argument("--window-size=1920,1080") #поменять размеры браузера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

driver.find_elements("xpath", "//a")[2].click()

driver.quit()  # Закрывает все окна и завершает сессию