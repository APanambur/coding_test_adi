from selenium.common.exceptions import StaleElementReferenceException, \
    NoSuchElementException, TimeoutException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from utils.logger import custom_logger


class SeleniumHelper(object):

    def __init__(self, driver):
        self.driver = driver
        self.timeout = 30
        self.log = custom_logger()

    def find_element(self, *locator):
        """
        Method to locate the web element
        :param locator: locator - tuple
        :return:element web element
        """
        element = None
        try:
            element = self.driver.find_element(*locator)
        except Exception as e:
            self.log.error("Exception {} while finding element".format(e))
        return element

    def find_elements(self, *locator):
        """
        Method to locate the web elements
        :param locator: locator - tuple
        :return: web elements - list
        """
        try:
            return self.driver.find_elements(*locator)
        except Exception as e:
            self.log.error("Exception {} while finding elements".format(e))
            return None

    def open_url(self, url):
        """
        Method to launch URL
        :param url: String - url
        :return:
        """
        try:
            self.driver.get(url)
        except Exception as e:
            self.log.error("Exception {0} while launching url".format(e))

    def element_visible(self, locator):
        try:
            element = WebDriverWait(self.driver, self.timeout).until(
                ec.visibility_of_element_located(locator))
            self.driver.execute_script("arguments[0].scrollIntoView();",
                                       element)
            self.log.info("Web element {0} : {1} "
                          "was visible".format(locator[0], locator[1]))
            return element
        except StaleElementReferenceException as st_elem_err:
            self.log.error("Stale element exception {0} was displayed during"
                           " element {1} : {2} location ".format(st_elem_err.msg,
                                                                 locator[0],
                                                                 locator[1]))
        except NoSuchElementException as no_such_elem_err:
            self.log.error("No such element exception {0} was displayed during"
                           "element {1} : {2} location".format(no_such_elem_err.msg,
                                                               locator[0],
                                                               locator[1]))
        except TimeoutException as time_out_err:
            self.log.error("Script timed out with message {0} during "
                           "element {1} : {2} location".format(time_out_err.msg,
                                                               locator[0],
                                                               locator[1]))

    def click(self, *locator):
        """
        Method to click on a element
        :param locator: locator - tuple
        :return: result - boolean
        """
        result = False
        try:
            element = self.element_visible(*locator)
            element.click()
            result = True
            self.log.info(
                "Web element {} successfully clicked".format(
                    locator))
        except NoSuchElementException as ex:
            self.log.error("Failed to click Web element {}"
                           " displayed with error {}".format(locator,
                                                              ex.msg))
        return result

    def enter(self, data, *locator):
        """
        Method to enter data
        :param data: input data
        :param locator: locator - tuple
        :return: status - boolean
        """
        try:
            element = self.element_visible(*locator)
            element.clear()
            element.send_keys(str(data))
            self.log.info("Web element {} was located "
                          "and entered with value : {}".
                          format(locator, str(data)))
            status = True
        except NoSuchElementException as no_such_elem_err:
            self.log.error("Failed to enter value {} for elements {},"
                           "displayed  error message {}".format(str(data),
                                                                 locator,
                                                                 no_such_elem_err.msg))
            status = False
        return status
