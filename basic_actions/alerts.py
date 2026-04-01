"""Модуль для работы с alert-окнами в браузере."""
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from webdriver_manager.chrome import ChromeDriverManager

chrome_options = Options()
chrome_options.add_argument("--window-size=1920,1080")

service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

driver.get("https://demoqa.com/")
time.sleep(1)
driver.find_element("xpath", "//a[@href='/alertsWindows']").click()
time.sleep(1)
driver.find_element("xpath", "//li[@id='item-1']//a[@href='/alerts']").click()

# BUTTON_1 = ("xpath", "//button[@id='alertButton']")
# wait.until(EC.element_to_be_clickable(BUTTON_1)).click()

BUTTON_2 = ("xpath", "//button[@id='promtButton']")
wait.until(EC.element_to_be_clickable(BUTTON_2)).click()

alert = wait.until(EC.alert_is_present())

#driver.switch_to.alert    закоммитил
#print(alert.text) #вывести текст алерта
#alert.accept() #принять алерт
#alert.dismiss()  #отклонить алерт
SEND_KEYS = "Hello World!"
alert.send_keys(SEND_KEYS) #Вписать текст в алерт
alert.accept() #принять алерт
text = driver.find_element(By.XPATH, "//span[@id='promptResult']").text
assert SEND_KEYS in text, f"Текст не передан в аллерт: {text}"

driver.quit()  # Закрывает все окна и завершает сессию
