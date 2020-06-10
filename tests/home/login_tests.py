from selenium import webdriver
from pages.home.login_page import LoginPage
import unittest
import pytest

@pytest.mark.usefixtures("oneTimeSetUp", "setUp") # oneTimeSetup and setUp are defined in conftest.py
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        self.lp = LoginPage(self.driver)

# ******* Test Methods

# TestCase 1: Verify Valid Login

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        self.lp.login("test@email.com", "abcabc")
        loginSuccessfulResult = self.lp.verifyLoginSuccessful()
        assert loginSuccessfulResult == True

# TestCase 2: Verify Invalid Login

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        self.lp.login("test@email.com", "abcabcabc")
        loginFailedResult = self.lp.verifyLoginFailed()
        assert loginFailedResult == True
