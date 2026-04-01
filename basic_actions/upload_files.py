"""Модуль для тестирования загрузки файлов на сервер."""
import os
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
service = Service(executable_path=ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)


driver.get("https://the-internet.herokuapp.com/upload")
time.sleep(1) #для наглядности
#print(f"{os.getcwd()}\\downloads\\test_upload.jpg")
upload_file = driver.find_element("xpath", "//input[@type='file']")
upload_file.send_keys(f"{os.getcwd()}/downloads/test_upload.jpg")

time.sleep(1)#для наглядности
driver.quit()  # Закрывает все окна и завершает сессию
