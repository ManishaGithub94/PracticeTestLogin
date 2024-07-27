import time

import pytest
from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from PageObjects.LoggedInPage import LoggedInPage
from selenium.webdriver.common.by import By


def test_positive_login(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.setUserName("student")
    login_page.setPassword("Password123")
    login_page.clickSubmit()

    assert "practicetestautomation.com/logged-in-successfully/" in driver.current_url,"URL does not contain 'logged-in-successfully/'"
    assert "Congratulations" in driver.page_source or "successfully logged in" in driver.page_source,"Success message not found in page source"
    assert driver.find_element(By.XPATH,login_page.button_logout_xpath).is_displayed(),"Logout button not displayed"


def test_negative_username(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.setUserName("wrongUser")
    login_page.setPassword("Password123")
    login_page.clickSubmit()
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(3)
    error_message = login_page.get_user_error_message()
    assert error_message == "Your username is invalid!", f"Expected 'Your username is invalid!', but got '{login_page.get_user_error_message()}'"

def test_negative_password(driver):
    login_page = LoginPage(driver)
    login_page.load()
    login_page.setUserName("student")
    login_page.setPassword("wrongPassword")
    login_page.clickSubmit()
    driver.execute_script("window.scrollBy(0, 200);")
    time.sleep(3)
    error_message = login_page.get_password_error_message()
    assert error_message == "Your password is invalid!", f"Expected 'Your password is invalid!', but got '{login_page.get_password_error_message()}'"
