from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoggedInPage:
    button_logout_xpath="//a[contains(text(),'Log out')]"
    text_successmessage_xpath="//strong[contains(text(),'Congratulations')]|//h1[contains(text(),'successfully logged in')]"

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def is_logout_button_displayed(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.button_logout_xpath))).is_displayed()


    def get_success_message(self):
        return self.wait.until(EC.presence_of_element_located((By.XPATH, self.text_successmessage_xpath))).text


