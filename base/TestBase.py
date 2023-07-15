import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from page.HomePage import HomePage
from page.SearchResultPage import SearchResultPage

class TestBase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.driver.get('http://congnongdan.vn')
        cls.home_page = HomePage(cls.driver)
        cls.search_result_page = SearchResultPage(cls.driver)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
