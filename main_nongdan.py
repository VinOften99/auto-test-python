import unittest
from base.TestBase import TestBase


class SearchTest(TestBase):
    def TE001(self):
        search_keyword = "từ khóa mẫu"
        self.assertTrue(self.home_page.is_search_input_displayed(), "Ô tìm kiếm không tồn tại")
        self.home_page.enter_search_keyword(search_keyword)
        self.assertEqual(self.home_page.get_search_input_value(), search_keyword, "Dữ liệu nhập vào không trùng khớp")

    def TE002(self):
        search_keyword = "nông"
        self.search_result_page.enter_search_keyword(search_keyword)
        self.search_result_page.click_search_button()
        self.assertTrue(self.search_result_page.get_number_of_results() > 0)

    def TE003(self):
        search_keyword = "nông"
        self.search_result_page.enter_search_keyword(search_keyword)
        self.search_result_page.press_enter_key()
        self.assertTrue(self.search_result_page.get_number_of_results() > 0)

    def TE004(self):
        search_keyword = "ádasdasdasdas"
        self.search_result_page.enter_search_keyword(search_keyword)
        self.search_result_page.click_search_button()
        self.assertFalse(self.search_result_page.get_number_of_results() > 0)

if __name__ == '__main__':
    unittest.main()
