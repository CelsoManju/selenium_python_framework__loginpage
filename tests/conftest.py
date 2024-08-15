import sys
sys.path.append("..")
import pytest
from selenium import webdriver
from pages.LoginPage import LoginPage

@pytest.fixture(scope="class")
def oneTimeSetUp(request):
    driver = webdriver.Chrome()
    baseUrl = "http://127.0.0.1:5500/index.html"
    driver.maximize_window()
    driver.implicitly_wait(3)

    if request.cls is not None:
        request.cls.driver = driver
        request.cls.baseUrl = baseUrl
        
    driver.get(baseUrl)

    yield driver
    driver.quit()

@pytest.fixture(autouse=True)
def setUp(request):
    request.cls.lp = LoginPage(request.cls.driver)
    request.cls.validusername = "admin"
    request.cls.validpassword = "password"
    request.cls.invalidusername = "admin123"
    request.cls.invalidpassword = "pwd123"
