import difflib

from selenium.webdriver.common.by import By

from selenium_test.framework.selenium_helper import SeleniumHelper
import allure


class MainPage(SeleniumHelper):
    """
        Class consists of main page objects and methods
    """

    def __init__(self, driver):
        SeleniumHelper.__init__(self, driver)
        self.driver = driver

    _search_textbox = (By.CSS_SELECTOR, 'input[id^="bodySearchInput"]')
    _lookup_button = (By.CSS_SELECTOR, 'input[value = "Look up"]')

    @allure.step("Verify main page is displayed")
    def verify_main_page(self):
        """
        method to verify home page is displayed
        :return: home page link element
        """
        element = self.element_visible(self._search_textbox)
        return element

    @allure.step("Enter text into search textbox and click on lookup button")
    def enter_text_and_search(self, text_val):
        self.enter(text_val, self._search_textbox)
        self.click(self._lookup_button)
