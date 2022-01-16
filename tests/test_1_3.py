import allure
import time
from pages.home_page import HomePage
class Test_1_3:
    @allure.severity(allure.severity_level.NORMAL)
    def test_01(self):
        home_page = HomePage()
        home_page.click_on_top_right_menu()
        home_page.my_account()
        time.sleep(3)
        home_page.login()
        text = home_page.find_login_text()
        assert text == 'Welcome'


