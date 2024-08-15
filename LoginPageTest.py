
import unittest
from tests.LoginTests import LoginTests

tc1 = unittest.TestLoader().loadTestsFromTestCase(LoginTests)

smokeTest = unittest.TestSuite([tc1])

unittest.TextTestRunner(verbosity=2).run(smokeTest)