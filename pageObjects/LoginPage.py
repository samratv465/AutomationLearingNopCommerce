from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_UserName_Id = "Email"
    textbox_Password_Id = "Password"
    btn_submit_xpath = "//button[@type='submit']"
    btn_logout_xpath = "//div[@id='navbarText']/ul/li[3]"

    def __init__(self, driver):
        self.driver = driver

    def setUserName(self, username):
        self.driver.find_element(By.ID, self.textbox_UserName_Id).clear()
        self.driver.find_element(By.ID, self.textbox_UserName_Id).send_keys(username)

    def setPassword(self, password):
        self.driver.find_element(By.ID, self.textbox_Password_Id).clear()
        self.driver.find_element(By.ID, self.textbox_Password_Id).send_keys(password)

    def clicksubmit(self):
        self.driver.find_element(By.XPATH, self.btn_submit_xpath).click()

    def clickLogout(self):
        self.driver.find_element(By.XPATH, self.btn_logout_xpath).click()

