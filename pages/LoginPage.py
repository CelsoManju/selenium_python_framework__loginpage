import time
import sys
sys.path.append("..")
from base.SeleniumDriver import SeleniumDriver
import utilities.custom_logger as cl
import logging

class LoginPage(SeleniumDriver):
    
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.log = cl.customLogger(logging.DEBUG)
    # Locators
        self.userNameId = "txt_inp_username"
        self.passwordId = "txt_inp_password"
        self.submitId = "//*[@id='btn_submit']"
        self.messageBoxId = "p_message"
        
    def enterUserName(self, data, locatorType):
        self.SendKeys(data, self.userNameId, locatorType)
        
    def clearUserName(self,locator,locatorType):
        self.clearTextBox(locator,locatorType)
        
    def clearPassword(self,locator,locatorType):
        self.clearTextBox(locator,locatorType)
        
    def enterPassword(self, data, locatorType):
        self.SendKeys(data, self.passwordId, locatorType)
        
    def clickLoginButton(self):
        self.elementClick(self.submitId, locatorType="xpath")

        
        
    def login(self, username="", password=""):
        self.clearUserName(self.userNameId,locatorType="id")
        self.enterUserName(username, locatorType="id")
        self.clearPassword(self.passwordId,locatorType="id")
        self.enterPassword(password, locatorType="id")
        self.clickLoginButton()
        time.sleep(5)

    def verifyLoginSuccessful(self):
        result = self.isElementPresent(self.messageBoxId, locatorType="id")      
        if result:
            self.log.info("Message box found")
            if result.text == "Login successful!":
                self.log.info("Message box text is :" + result.text) 
                self.takeScreenshot("verifyLoginSuccessful_true.png")
                return True
            else:
                self.log.error("Message box text is :" + result.text)
                self.takeScreenshot("verifyLoginSuccessful_false.png")
                return False
        else:
            self.log.error("Message box not found")
            return False
        
    def verifyLoginfailed(self):
        time.sleep(5)
        result = self.isElementPresent(self.messageBoxId, locatorType="id")
        if result :
            self.log.info("Message box found")
            if result.text == "Invalid username or password.":
                self.log.info("Message box text is :" + result.text)
                self.takeScreenshot("verifyLoginfailed_true.png")
                return True
        else:
            self.log.info("Message box text is :" + result.text)
            self.takeScreenshot("verifyLoginfailed_false.png")
            return False
