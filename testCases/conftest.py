import pytest
from selenium import webdriver
from utilities.readProperties import ReadConfig

baseurl = ReadConfig.getApplicationUrl()

def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser", action = "store", default = "chrome", help = "Specify the browser: chrome or firefox or edge")

@pytest.fixture()
def browser(request):  ##This will return the Browser value to setup the method
    return request.config.getoption("--browser")

########### browser setup ################
@pytest.fixture()
def setup(browser):
    global driver
    if browser=='chrome':
        driver = webdriver.Chrome()
        driver.maximize_window()
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

@pytest.fixture()
def setup_and_teardown(setup, request):
    driver = setup
    print("****Opening Base URL****")
    driver.get(baseurl)
    request.cls.driver = driver
    yield
    driver.close()

def pytest_html_report_title(report):
    report.title = "Automation HTML Report"

def _capture_screenshot(name):
    # screenshot_path = "./Screenshots/" + name
    # print("screenshot_path=" + screenshot_path)
    driver.get_screenshot_as_file(name)

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # now = datetime.now()
    pytest_html = item.config.pluginmanager.getplugin('html')
    outcome = yield
    report = outcome.get_result()
    extra = getattr(report, 'extra', [])
    if report.when == 'call' or report.when == "setup":
        xfail = hasattr(report, 'wasxfail')
        if (report.skipped and xfail) or (report.failed and not xfail):
            file_name = report.nodeid.replace("::", "_") + ".png"
            print("file_name=" + file_name)
            # file_name = "screenshot" + now.strftime("%S%H%d%m%Y") + ".png"
            _capture_screenshot(file_name)
            if file_name:
                html = '<div><img src="%s" alt="screenshot" style="width:304px;height:228px;" ' \
                       'onclick="window.open(this.src)" align="right"/></div>' % file_name
                extra.append(pytest_html.extras.html(html))
        report.extra = extra
