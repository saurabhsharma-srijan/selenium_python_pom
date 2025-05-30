from selenium.webdriver.common.by import By

class ContactPage:
    ## Locators on login page
    link_contact_xpath = "//a[contains(text(),'Contact us')]"
    submit_xpath = "//input[@type='submit']"

    ## constructor to initiate the driver, it will invoke at the time of object creation
    def __init__(self, driver):
        self.driver = driver

    ## actions on login page

    def clickContactLink(self):
        self.driver.find_element(By.XPATH,self.link_contact_xpath).click()

    def clickSubmit(self):
        self.driver.find_element(By.XPATH,self.submit_xpath)
