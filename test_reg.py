import pytest
import time
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select


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
    hname.send_keys("ZZ")
    hlastname = driver.find_element(By.ID, "signupLastName")
    hlastname.send_keys("YY")
    hemail = driver.find_element(By.ID, "signupEmail")
    hemail.send_keys("ZY@mail.com")
    hpassword = driver.find_element(By.ID, "signupPassword")
    hpassword.send_keys("15071981Aa")
    hpassword1 = driver.find_element(By.ID, "signupRepeatPassword")
    hpassword1.send_keys("15071981Aa")
    hbtnregister = driver.find_element(By.CSS_SELECTOR, "body > ngb-modal-window > div > div > app-signup-modal > div.modal-footer > button")
    hbtnregister.click()
    time.sleep(5)


def test_add_car(driver):
    hbtnadd = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[1]/button")
    time.sleep(5)
    hbtnadd.click()
    hautoname = driver.find_element(By.ID, "addCarBrand")
    hautoname.click()
    time.sleep(2)
    se1 = Select(driver.find_element(By.ID, "addCarBrand"))
    se1.select_by_value("2: 3")
    time.sleep(2)
    hmodel = driver.find_element(By.ID, "addCarModel")
    hmodel.click()
    se2 = Select(driver.find_element(By.ID, "addCarModel"))
    se2.select_by_value("7: 13")
    hmodel.click()
    hmile = driver.find_element(By.ID, "addCarMileage")
    hmile.send_keys("25")
    hbtnadd1 = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-add-car-modal/div[3]/button[2]")
    hbtnadd1.click()
    time.sleep(5)


def test_expence(driver):
    hexpbtn1 = driver.find_element(By.XPATH,"/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-garage/div/div[2]/div/ul/li[1]/app-car/div/div[1]/div[2]/button[2]")
    hexpbtn1.click()
    time.sleep(5)
    hmleage1 = driver.find_element(By.ID, "addExpenseMileage")
    hmleage1.clear()
    hmleage1.send_keys("30")
    hliters1 = driver.find_element(By.ID, "addExpenseLiters")
    hliters1.send_keys("25")
    htotal1 = driver.find_element(By.ID, "addExpenseTotalCost")
    htotal1.send_keys("7000")
    time.sleep(3)
    hadd2btn1 = driver.find_element(By.XPATH,"/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
    hadd2btn1.click()
    time.sleep(3)
    hexpbtn2 = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-fuel-expenses/div/div[1]/div/button")
    hexpbtn2.click()
    time.sleep(5)
    hmleage2 = driver.find_element(By.ID, "addExpenseMileage")
    hmleage2.clear()
    hmleage2.send_keys("40")
    hliters2 = driver.find_element(By.ID, "addExpenseLiters")
    hliters2.send_keys("40")
    htotal2 = driver.find_element(By.ID, "addExpenseTotalCost")
    htotal2.send_keys("8250")
    time.sleep(3)
    hadd2btn2 = driver.find_element(By.XPATH,"/html/body/ngb-modal-window/div/div/app-add-expense-modal/div[3]/button[2]")
    hadd2btn2.click()
    time.sleep(5)
def test_remove(driver):
    hsettings = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[1]/nav/div/a[2]")
    hsettings.click()
    time.sleep(2)
    hdeletebtn = driver.find_element(By.XPATH, "/html/body/app-root/app-global-layout/div/div/div/app-panel-layout/div/div/div/div[2]/div/app-settings/div/div[2]/div/div[5]/div/button")
    hdeletebtn.click()
    time.sleep(2)
    hremove = driver.find_element(By.XPATH, "/html/body/ngb-modal-window/div/div/app-remove-account-modal/div[3]/button[2]")
    hremove.click()
    driver.close()
