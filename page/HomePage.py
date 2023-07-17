from selenium.webdriver.common.by import By


class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.search_input = self.driver.find_element(By.XPATH, '//input[@placeholder="Nội dung tìm kiếm..."]')

    def is_search_input_displayed(self):
        return self.search_input.is_displayed()

    def enter_search_keyword(self, keyword):
        self.search_input.clear()
        self.search_input.send_keys(keyword)

    def get_search_input_value(self):
        return self.search_input.get_attribute("value")
