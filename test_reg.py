import pytest
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


@pytest.fixture(scope="module")
def driver():
    print("Init driver")
    driver = Chrome()
    yield driver
    print("Quit driver")
    driver.quit()

def test_reg_errortext(driver):
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")
    driver.maximize_window()
    hbtnsingup = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-guest-layout/div/app-home/section/div/div/div[1]/div/button")
    hbtnsingup.click()
    hname = driver.find_element(By.ID, "signupName")
    hname.send_keys("Isaak")
    hlastname = driver.find_element(By.ID, "signupLastName")
    hlastname.send_keys("Newton")
    hemail = driver.find_element(By.ID, "signupEmail")
    hemail.send_keys("isaak@mail.com")
    hpassword = driver.find_element(By.ID, "signupPassword")
    hpassword.send_keys("15071981Aa")
    hpassword1 = driver.find_element(By.ID, "signupRepeatPassword")
    hpassword1.send_keys("15071981Aa")
    hbtnregister = driver.find_element(By.CSS_SELECTOR, "body > ngb-modal-window > div > div > app-signup-modal > div.modal-footer > button")
    hbtnregister.click()
    time.sleep(5)
    time.sleep(10)
    driver.close()
