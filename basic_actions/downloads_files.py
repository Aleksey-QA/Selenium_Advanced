import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
prefs = {
    "download.default_directory": fr"{os.getcwd()}\downloads"
}
print(prefs)
chrome_options.add_experimental_option("prefs", prefs)
#chrome_options.add_argument("--window-size=1920,1080") #поменять размеры браузера
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

driver.get("https://the-internet.herokuapp.com/download")

driver.find_elements("xpath", "//a")[2].click()

driver.quit()  # Закрывает все окна и завершает сессию
