from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    URL = "https://practicetestautomation.com/practice-test-login/"
    textbox_username_id="username"
    textbox_password_id="password"
    button_submit_xpath="//button[@id='submit']"
    button_logout_xpath="//a[contains(text(),'Log out')]"
    usererrormessage="//div[contains(text(),'Your username is invalid!')]"
    passworderrormessage="//div[contains(text(),'Your password is invalid!')]"


    def __init__(self,driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)

    def load(self):
        self.driver.get(self.URL)

    def setUserName(self,username):
        self.driver.find_element(By.ID,self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID,self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickSubmit(self):
        self.driver.find_element(By.XPATH,self.button_submit_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH,self.button_logout_xpath).click()

    def get_user_error_message(self):
        error_element =  self.driver.find_element(By.XPATH, self.usererrormessage)
        print(error_element.text)
        return error_element.text

    def get_password_error_message(self):
        passworderror =  self.driver.find_element(By.XPATH, self.passworderrormessage)
        print(passworderror.text)
        return passworderror.text







