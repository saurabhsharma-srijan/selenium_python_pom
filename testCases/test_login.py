from pageObjects.LoginPage import LoginPage
from utilities.customLogger import LogGen
from utilities.readProperties import ReadConfig

class Test_Login:
    baseurl = ReadConfig.getApplicationUrl()
    username = ReadConfig.getUserEmail()
    password = ReadConfig.getUserPassword()
    logger = LogGen.loggen()

## To using class variable we have to use self keyword

    def test_loginPageTitle(self,setup):
        self.logger.info("****Started Login page title test ****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.clickLoginLink()
        act_title = self.driver.title
        if act_title == "Automation Exercise - Signup / Login":
            self.logger.info("**** Login page title test passed ****")
            assert True
        else:
            self.logger.error("**** Login page title test failed ****")
            self.driver.save_screenshot("/Users/saurabh.sharma/PycharmProjects/pythonProjectPOM/Screenshots/test_loginPageTitle.png")
            assert False
        print("on login page screen")
        self.driver.close()

    def test_login(self,setup):
        self.logger.info("****Started Login Test****")
        self.driver = setup
        self.logger.info("****Opening URL****")
        self.driver.get(self.baseurl)
        self.lp = LoginPage(self.driver)
        self.lp.clickLoginLink()
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickSubmitButton()
        act_title = self.driver.title
        if act_title == "Automation Exercise":
            self.logger.info("****Login test passed ****")
            assert True
        else:
            self.logger.error("****Login test failed ****")
            self.driver.save_screenshot("/Users/saurabh.sharma/PycharmProjects/pythonProjectPOM/Screenshots/test_login.png")
            assert False
        print("on dashboard page screen")
        self.lp.clickLogoutLink()
        self.driver.close()
















