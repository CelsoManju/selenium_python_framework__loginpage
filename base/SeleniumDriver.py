from selenium.webdriver.common.by import By
from traceback import print_stack
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import *
import utilities.custom_logger as cl
import logging

class SeleniumDriver():
    def __init__(self, driver):
        self.driver = driver
        self.log = cl.customLogger(logging.DEBUG)

    def getbyType(self, locatorType):
        locatorType = locatorType.lower()
        if locatorType == "id":
            return By.ID
        if locatorType == "name":
            return By.NAME
        if locatorType == "xpath":
            return By.XPATH
        if locatorType == "link":
            return By.LINK_TEXT
        if locatorType == "css":
            return By.CSS_SELECTOR
        if locatorType == "tag":
            return By.TAG_NAME
        if locatorType == "class":
            return By.CLASS_NAME
        else:
            self.log.error("Locator type " + locatorType + " not found or not supported")
        return False

    def getElement(self, locator, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            byType = self.getbyType(locatorType)
            element = self.driver.find_element(byType, locator)
            self.log.info("Element Found with locator: " + locator + " and locatorType: " + locatorType)
        except:
            self.log.error("Element not Found with locator: " + locator + " and locatorType: " + locatorType)
        return element

    def elementClick(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.click()
            self.log.info("Clicked on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot click on element with locator: " + locator + " locatorType: " + locatorType)

    def SendKeys(self, data, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Cannot send data on element with locator: " + locator + " locatorType: " + locatorType)

    def isElementPresent(self, locator, locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element found")
                return element
        except:
            self.log.error("Element not found")
        return False

    def waitForElement(self, locator, locatorType="id", timeout=10, pollFrequency=0.5):
        element = None
        try:
            byType = self.getbyType(locatorType)
            self.log.info("Waiting for maximum :: " + str(timeout) + " :: seconds for element to be clickable")
            wait = WebDriverWait(self.driver, timeout, poll_frequency=pollFrequency,
                                 ignored_exceptions=[NoSuchElementException,
                                                     ElementNotVisibleException,
                                                     ElementNotSelectableException])
            element = wait.until(EC.element_to_be_clickable((byType, locator)))
            self.log.info("Element appeared on the web page")
        except:
            self.log.error("Element did not appear on the web page")
            print_stack()
        return element

    def takeScreenshot(self, filename):
        try:
            self.driver.save_screenshot(filename)
            self.log.info("Screenshot saved as " + filename)
        except:
            self.log.error("Failed to save screenshot")
    def clearTextBox(self,locator, locatorType="id"):
        try:
            byType = self.getbyType(locatorType)            
            element = self.getElement(locator, byType)
            element.clear()
            self.log.info("cleared data on element with locator: " + locator + " locatorType: " + locatorType)
        except:
            self.log.error("Did not clear send data on element with locator: " + locator + " locatorType: " + locatorType)
            
