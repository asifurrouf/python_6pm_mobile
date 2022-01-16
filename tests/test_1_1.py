import allure
from pages.home_page import HomePage
class Test_1_1:
    @allure.severity(allure.severity_level.NORMAL)
    def test_01(self):
        # open = BaseTest()
        # open.setUp()
        home_page = HomePage()
        home_page.click_on_search_box()
        # assert text == 'pant'





