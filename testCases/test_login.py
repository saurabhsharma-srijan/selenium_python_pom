from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class Test_Login:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()

####To using class variable we have to use self keyword
    def test_loginPageTitle(self):
        print("****Started Login page title test ****")
        self.lp = LoginPage(self.driver)
        self.lp.clickLoginLink()
        act_title = self.driver.title
        if act_title == "Automation Exercise - Signup / Login":
            print("**** Login page title test passed ****")
            assert True
            print("on login page screen")
        else:
            print("**** Login page title test failed ****")
            assert False

    def test_login(self):
        print("****Started Login Test****")
        self.lp = LoginPage(self.driver)
        self.lp.clickLoginLink()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSubmitButton()
        act_title = self.driver.title
        if act_title == "Automation Exercise":
            print("****Login test passed ****")
            assert True
            print("on dashboard page screen")
        else:
            print("****Login test failed ****")
            assert False
        self.lp.clickLogoutLink()
