import pytest
from pageObjects.LoginPage import LoginPage
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from utilities import excel_utils
import time

class Test_002_DDT_Login():
    baseURL = ReadConfig.getApplicationUrl()
    path = "/Users/saurabh.sharma/PycharmProjects/pythonProjectPOM/TestData/login_data.xlsx"
    logger = LogGen.loggen()  # Logger

    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("******* Starting Test_002_DDT_Login Test **********")
        self.logger.info("******* Starting Login DDT Test **********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()
        self.lp = LoginPage(self.driver)
        self.lp.clickLoginLink()

        self.rows = excel_utils.getRowCount(self.path, 'Sheet1')
        print('Number of rows...',self.rows)
        status_list=[]

        for r in range(2,self.rows+1):
            self.user = excel_utils.readData(self.path,'Sheet1',r,1)
            self.password = excel_utils.readData(self.path, 'Sheet1', r, 2)
            self.exp = excel_utils.readData(self.path, 'Sheet1', r, 3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickSubmitButton()
            time.sleep(2)
            act_title=self.driver.title
            exp_title="Automation Exercise"

            if act_title == exp_title:
                print("page title is expected")
                if self.exp=='Yes':
                    self.logger.info("**** test data is passed ****")
                    status_list.append("Pass")
                    self.lp.clickLogoutLink()
                elif self.exp=='No':
                    self.logger.info("**** test data is failed ****")
                    status_list.append("Fail")
                    self.lp.clickLogoutLink()

            elif act_title != exp_title:
                if self.exp == 'Yes':
                    self.logger.info("**** test data is failed ****")
                    status_list.append("Fail")
                elif self.exp == 'No':
                    self.logger.info("**** test data is passed ****")
                    status_list.append("Pass")
        print(status_list)
        if "Fail" not in status_list:
            self.logger.info("******* DDT Login test passed **********")
            self.driver.close()
            assert True
        else:
            self.logger.error("******* DDT Login test failed **********")
            self.driver.close()
            assert False
        self.logger.info("******* End of Login Data Driven Test **********")