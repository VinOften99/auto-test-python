from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class SearchResultPage:
    def __init__(self, driver):
        self.driver = driver

    def enter_search_keyword(self, keyword):
        search_box = self.driver.find_element(By.XPATH, '//input[@placeholder="Nội dung tìm kiếm..."]')
        search_box.clear()
        search_box.send_keys(keyword)

    def press_enter_key(self):
        search_box = self.driver.find_element(By.XPATH, '//input[@placeholder="Nội dung tìm kiếm..."]')
        search_box.send_keys(Keys.RETURN)

    def click_search_button(self):
        search_button = self.driver.find_element(By.XPATH, '//span[@class="input-group-addon search-span"]')
        search_button.click()

    def get_number_of_results(self):
        results_container = self.driver.find_element(By.XPATH, '//div[@class="col-md-12 col-sm-12 padding-right0"]')
        result_items = results_container.find_elements(By.XPATH, '//div[@class="row padding-topbot5"]')
        return len(result_items)