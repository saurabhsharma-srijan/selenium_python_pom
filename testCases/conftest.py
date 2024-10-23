import pytest
from pytest_metadata.plugin import metadata_key
from selenium import webdriver

def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser", action = "store", default = "chrome", help = "Specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")

########### browser setup ################
@pytest.fixture()
def setup(browser):
    global driver
    if browser=='chrome':
        driver = webdriver.Chrome()
        print("Launching chrome browser.........")
    elif browser=='firefox':
        driver = webdriver.Firefox()
        print("Launching firefox browser.........")
    elif browser=='edge':
        driver = webdriver.Edge()
        print("Launching edge browser.........")
    else:
        raise ValueError("Unsupported Browser")
    return driver

########### pytest HTML Report ################
# It is hook for Adding Environment info to HTML Report
def pytest_configure(config):
    config.stash[metadata_key]['Project Name'] = 'nop Commerce'
    config.stash[metadata_key]['Module Name'] = 'Customers login'
    config.stash[metadata_key]['Tester Name'] = 'Saurabh'

# It is hook for delete/Modify Environment info to HTML Report
@pytest.mark.optionalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)