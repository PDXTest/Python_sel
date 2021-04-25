import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


class AddUser:

    def __init__(self, driver):
        self.driver = driver

    Adminlink = (By.XPATH, "//b[contains(text(),'Admin')]")
    Usermgmt = (By.XPATH, "//a[@id='menu_admin_UserManagement']")
    Userlink = (By.XPATH, "//a[@id='menu_admin_viewSystemUsers']")
    Add = (By.XPATH, " //input[@id='btnAdd']")
    Name = (By.XPATH, "//input[@id='systemUser_employeeName_empName']")

    def adminlink(self):
        element_to_hover_over = self.driver.find_element(*AddUser.Adminlink)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

        time.sleep(1)
        element_to_hover_over = self.driver.find_element(*AddUser.Usermgmt)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.perform()

        time.sleep(1)
        element_to_hover_over = self.driver.find_element(*AddUser.Userlink)
        hover = ActionChains(self.driver).move_to_element(element_to_hover_over)
        hover.click().perform()

    def clickaddbutton(self):
        self.driver.find_element(*AddUser.Add).click()

    def getname(self):
        return self.driver.find_element(*AddUser.Name)
