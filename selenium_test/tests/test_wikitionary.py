import os
from os.path import dirname, abspath
import pytest

from selenium_test.pages.main_page import MainPage
from selenium_test.pages.search_result_page import SearchResultPage
from utils import parser

params = parser.parse_json(os.path.join(
    os.path.join(dirname(dirname(abspath(__file__))), 'resources'),
    'test_wiktionary.json'),
    ['search_item', 'url', 'definition'])


@pytest.mark.parametrize('search_item,url,definition', params)
def test_wiktionary(init_driver, search_item, url, definition):
    driver = init_driver
    main_page = MainPage(driver)
    search_result_page = SearchResultPage(driver)
    assert main_page.verify_main_page(), 'Main Page is not displayed'
    main_page.enter_text_and_search(search_item)
    assert search_result_page.verify_definition(definition), \
        'Expected definition ' + definition + ' not found in Result Page for ' \
        + search_item
