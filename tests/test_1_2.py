import allure
from pages.home_page import HomePage
class Test_1_2:
    @allure.severity(allure.severity_level.NORMAL)
    def test_01(self):
        home_page = HomePage()
        text = home_page.bag_summary()
        assert text == 'Bag Summary'

