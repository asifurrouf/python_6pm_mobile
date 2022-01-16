import allure
import time
from pages.home_page import HomePage
class Test_1_4:
    @allure.severity(allure.severity_level.NORMAL)
    def test_01(self):
        home_page = HomePage()
        home_page.click_on_top_right_menu()
        home_page.favourites()
        time.sleep(5)
        home_page.login()
        time.sleep(2)
        text = home_page.find_favourites_text()
        assert text == 'Favorites'


