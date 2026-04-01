import time

from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait

options = Options()
options.add_argument("--window-size=1980,1080")
driver = webdriver.Chrome(options=options)
wait = WebDriverWait(driver, 10, poll_frequency=1)

BUTTON_EDIT_LOCATOR = ("xpath", "//button[@data-action='edit']")
BUTTON_CLICK_ME_LOCATOR = ("xpath", "//button[@name='my-button']")

driver.get("http://uitestingplayground.com/frames")

wait.until(EC.frame_to_be_available_and_switch_to_it("frame-outer"))
print("Переключились во внешний фрейм")
driver.find_element(*BUTTON_CLICK_ME_LOCATOR).click()
time.sleep(2)
wait.until(EC.frame_to_be_available_and_switch_to_it("frame-inner"))
print("Переключились во внутренний фрейм")
button = wait.until(EC.element_to_be_clickable(BUTTON_EDIT_LOCATOR))
button.click()
time.sleep(2)
driver.find_element(*BUTTON_CLICK_ME_LOCATOR).click()
time.sleep(1)
