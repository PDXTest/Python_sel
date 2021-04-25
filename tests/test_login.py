import time

from PageObjects.LoginPage import LoginPage
from utilities.BaseClass import BaseClass


class TestOrangeHRM(BaseClass):

    def test_Login(self):
        log = self.getLogger()
        loginpage = LoginPage(self.driver)
        loginpage.getUsername().send_keys("Admin")
        log.info("first name is entered")
        loginpage.getPassword().send_keys("admin123")
        log.info("Password is entered")
        loginpage.submitform().click()
        log.info("Login button is clicked")

        alertText = loginpage.getdashboard().text
        print(alertText)

        assert ("Dashboard" in alertText)




