import difflib

from selenium.webdriver.common.by import By

from selenium_test.framework.selenium_helper import SeleniumHelper
import allure


class SearchResultPage(SeleniumHelper):
    """
        Class consists of search results page objects and methods
    """

    def __init__(self, driver):
        SeleniumHelper.__init__(self, driver)
        self.driver = driver

    _definitions_content = (By.CSS_SELECTOR, '#mw-content-text ol > li')

    @allure.step("Verify expected definition is present in the search "
                 "result page")
    def verify_definition(self, expected_definition):
        definition_list = self.find_elements(*self._definitions_content)
        for elem in definition_list:
            if difflib.SequenceMatcher(None, expected_definition,
                                       elem.text).ratio() > 0.8:
                return True
        return False
