from base.selenium_driver import SeleniumDriver
from utilities import custom_logger as cl
import logging


class LoginPage(SeleniumDriver):

    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

# Locators

    _login_link = "Login"
    _email_field = "user_email"
    _password_field = "user_password"
    _login_button = "commit"

# Events

    def clickLoginLink(self):
        self.elementClick(self._login_link, locatorType="link")

    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="id")

    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="id")

    def clickLoginButton(self):
        self.elementClick(self._login_button, locatorType="name")

    def clearEmailIdField(self):
        self.clearEditBox(self._email_field, locatorType="id")

    def clearPasswordIdField(self):
        self.clearEditBox(self._password_field, locatorType="id")

# ----------------------------
# Page Functionality / Actions

    def login(self, email="", password=""):     # By default passing the email and password as empty
        self.clickLoginLink()
        self.clearEmailIdField()
        self.clearPasswordIdField()
        self.enterEmail(email)
        self.enterPassword(password)
        self.clickLoginButton()

    def verifyLoginSuccessful(self):
        result = self.isElementPresent("//img[@class='gravatar']", locatorType="xpath")
        return result

    def verifyLoginFailed(self):
        result = self.isElementPresent("//*[contains(text(), 'Invalid email or password')]", locatorType="xpath")
        return result
