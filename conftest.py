import time

import allure
import pytest
from selenium.webdriver import ChromeOptions, Chrome
from webdriver_manager.chrome import ChromeDriverManager


def pytest_addoption(parser):
    """ Command line options:
        Example of allowing pytest to accept a command line option  """
    parser.addoption("-B", "--browser",
                     dest="browser",
                     default="chrome",
                     help="Browser. Valid options are chrome or headlesschrome")


@pytest.fixture(scope="session")
def browser(request):
    """ pytest fixture for browser
    :return:
    """
    return request.config.getoption("browser")


def get_driver(browser):
    """  method to instantiate the browser type  """
    driver = None
    if browser.lower() == 'chrome':
        chrome_options = ChromeOptions()
        chrome_options.add_argument("--start-maximized")
        driver = Chrome(executable_path=ChromeDriverManager().install(),
                        options=chrome_options)
    elif browser.lower() == 'headless':
        crome_options = ChromeOptions()
        crome_options.add_argument('headlesschrome')
        crome_options.add_argument("--start-maximized")
        """ this line is required for headless browser to run successfully """
        crome_options.add_argument('--window-size=1920x1080')
        driver = Chrome(executable_path=ChromeDriverManager().install(), options=crome_options)
    return driver


@pytest.fixture
def init_driver(request, browser, url):
    """  method to instantiate the driver """
    driver = get_driver(browser)
    driver.get(str(url))
    time.sleep(5)
    tests_failed_before_module = request.session.testsfailed
    yield driver

    """ tear down after the tests """
    after = request.session.testsfailed - tests_failed_before_module
    if after > tests_failed_before_module:
        allure.attach(driver.get_screenshot_as_png(), name='error_screenshot',
                      attachment_type=allure.attachment_type.PNG)
    driver.quit()