import sys
sys.path.append("..")
import pytest
import unittest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    
    log =  cl.customLogger(logging.DEBUG)
    
    @pytest.mark.run(order=1)
    def test_validLogin(self):        
        self.lp.login(self.validusername, self.validpassword)        
        result2 = self.lp.verifyLoginSuccessful()
        self.log.info("test_validLogin result" + str(result2) )
        assert result2 is True
        
    @pytest.mark.run(order=2)
    def test_invalidLogin(self):        
         self.lp.login(self.invalidusername, self.invalidpassword)
         result = self.lp.verifyLoginfailed()
         self.log.info("test_validLogin result" + str(result) )
         assert result is True
