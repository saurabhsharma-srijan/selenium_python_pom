from selenium.webdriver.common.by import By

class LoginPage:
    ## Locators on login page
    textbox_username_name = "email"
    textbox_password_name = "password"
    loginButton_submit_xpath = "//button[@data-qa='login-button']"
    link_login_xpath = "//a[contains(text(),'Signup / Login')]"
    link_logout_xpath = "//a[contains(text(),'Logout')]"

    ## constructor to initiate the driver, it will invoke at the time of object creation
    def __init__(self, driver):
        self.driver = driver

    ## actions on login page
    def setUserName(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).clear()
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_password_name).clear()
        self.driver.find_element(By.NAME,self.textbox_password_name).send_keys(password)

    def clickSubmitButton(self):
        self.driver.find_element(By.XPATH,self.loginButton_submit_xpath).click()

    def clickLoginLink(self):
        self.driver.find_element(By.XPATH,self.link_login_xpath).click()

    def clickLogoutLink(self):
        self.driver.find_element(By.XPATH,self.link_logout_xpath).click()






