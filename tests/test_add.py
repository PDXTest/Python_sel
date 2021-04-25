import pytest
import time

from PageObjects.AddUser import AddUser
from PageObjects.LoginPage import LoginPage
from TestData1.Addtestdata import AddUserData

from utilities.BaseClass import BaseClass


class Test_Add(BaseClass):

    def test_adduser(self, getData):
        log1 = self.getLogger()
        log1.info("first name is entered")
        loginpage = LoginPage(self.driver)
        loginpage.getUsername().send_keys("Admin")
        log1.info("first name is entered")
        loginpage.getPassword().send_keys("admin123")
        log1.info("first name is entered")
        loginpage.submitform().click()
        time.sleep(1)

        adduser = AddUser(self.driver)
        adduser.adminlink()

        time.sleep(3)
        adduser.clickaddbutton()
        time.sleep(1)
        print(getData["Fname"])
        #Webelement = self.driver.find_element_by_id("systemUser_employeeName_empName")
        #print(Webelement)
        #Webelement.send_keys("Raje")
        adduser.getname().send_keys(getData["Fname"])

        print("Add User")

    @pytest.fixture(params=AddUserData.getTestData("Testcase2"))
    def getData(self, request):
        return request.param
