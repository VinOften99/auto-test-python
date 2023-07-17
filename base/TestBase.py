import unittest
from selenium import webdriver
from page.HomePage import HomePage
from page.SearchResultPage import SearchResultPage


class TestBase(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get('http://congnongdan.vn')
        self.home_page = HomePage(self.driver)
        self.search_result_page = SearchResultPage(self.driver)

    @classmethod
    def tearDown(self):
        self.driver.quit()
