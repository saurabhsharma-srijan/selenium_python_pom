from pageObjects.ContactPage import ContactPage
import pytest

@pytest.mark.usefixtures("setup_and_teardown")
class Test_Contact:
    def test_contactPageTitle(self):
        print("****Started Contact page title test****")
        self.cp = ContactPage(self.driver)
        self.cp.clickContactLink()
        act_title = self.driver.title
        if act_title == "Automation Exercise - Contact Us123":
            print("**** Contact page title test passed ****")
            assert True
            print("on Contact page screen")
        else:
            print("**** Contact page title test failed ****")
            assert False

    def test_getInTouch(self):
        print("****Started get In Touch label test****")
        self.cp = ContactPage(self.driver)
        self.cp.clickContactLink()
        self.cp.clickSubmit()
