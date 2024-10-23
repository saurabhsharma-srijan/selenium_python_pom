from selenium.webdriver.common.by import By

class Contact_Page:
    ## Locators on contact page
    title_getintouch_xpath = "//h2[contains(text(),'Get In Touch')]"
    textbox_field_name = "name"
    textbox_password_name = "password"
    textbox_subject_name = "subject"
    textarea_message_name = "message"
    contact_submit_name = "submit"
    link_contact_xpath = "//a[contains(text(),'Contact us')]"
    success_message_xpath = "//div[@class='status alert alert-success']"

    ## constructor to initiate the driver, it will invoke at the time of object creation
    def __init__(self, driver):
        self.driver = driver

    ## actions on login page
    def setName(self,username):
        self.driver.find_element(By.NAME,self.textbox_username_name).clear()
        self.driver.find_element(By.NAME,self.textbox_username_name).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.NAME,self.textbox_password_name).clear()
        self.driver.find_element(By.NAME,self.textbox_password_name).send_keys(password)

    def clickSubmitButton(self):
        self.driver.find_element(By.XPATH,self.loginButton_submit_xpath).click()

    def clickContactLink(self):
        self.driver.find_element(By.XPATH,self.link_login_xpath).click()





