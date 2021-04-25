from selenium.webdriver.common.by import By


class LoginPage:

    def __init__(self, driver):
        self.driver = driver

    username = (By.ID, "txtUsername")
    password = (By.ID, "txtPassword")
    submit = (By.ID, "btnLogin")
    dashboard = (By.XPATH, "//h1[contains(text(),'Dashboard')]")

    def getUsername(self):
        return self.driver.find_element(*LoginPage.username)

    def getPassword(self):
        return self.driver.find_element(*LoginPage.password)

    def submitform(self):
        return self.driver.find_element(*LoginPage.submit)

    def getdashboard(self):
        return self.driver.find_element(*LoginPage.dashboard)
