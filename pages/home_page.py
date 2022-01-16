from selenium.webdriver.common import keys
from appium.webdriver.common.mobileby import By
from appium import webdriver

import time


class HomePage:

    desired_cap = {
        "appium:deviceName": "95fdd773",
        "platformName": "Android",
        "appium:app": "C:/Users/FoysalAhmed/Desktop/QUPS_assigmnets/6pm_android/6PM_v2.1.1.apk"
    }

    driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)

    def click_on_search_box(self):
        # self.driver.implicitly_wait(50)
        search_box = self.driver.find_element(By.ID, 'com.zappos.android.sixpmFlavor:id/menu_search')
        search_box.click()

        # self.driver.implicitly_wait(20)
        time.sleep(2)
        search_box_type = self.driver.find_element(By.ID, 'com.zappos.android.sixpmFlavor:id/search_src_text')
        search_box_type.clear()
        search_box_type.send_keys('shirts')

    def find_searched_text(self):
        text_element = self.driver.find_element_by_xpath(
            '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[1]')
        text = text_element.text
        return text

    def bag_summary(self):
        cart = self.driver.find_element(By.ID, 'com.zappos.android.sixpmFlavor:id/icon')
        cart.click()
        self.driver.implicitly_wait(10)

        cart_text = self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.view.ViewGroup/android.view.ViewGroup/android.widget.TextView[1]')
        text = cart_text.text
        return text
    def click_on_top_right_menu(self):
        self.driver.find_element(By.XPATH, '//android.widget.ImageView[@content-desc="More options"]').click()
        self.driver.implicitly_wait(20)

    def my_account(self):
        self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ListView/android.widget.LinearLayout[1]').click()
        self.driver.implicitly_wait(50)
        time.sleep(10)
    def login(self):
        #types email
        self.driver.implicitly_wait(30)
        email = self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[3]/android.widget.EditText')
        time.sleep(10)
        email.click()
        self.driver.implicitly_wait(10)
        # email.clear()
        email.send_keys('foysal.cse.nsu@gmail.com')
        time.sleep(5)
        # types password
        password = self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[5]/android.widget.EditText')
        password.click()
        time.sleep(5)
        password.send_keys('6pm.com')
        time.sleep(5)

        # clicks sign-in button
        self.driver.back()
        time.sleep(5)
        submit = self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.view.ViewGroup/android.webkit.WebView/android.webkit.WebView/android.view.View/android.view.View[2]/android.view.View[8]/android.widget.Button')

        submit.click()
        time.sleep(5)

    def find_login_text(self):
        login_text = self.driver.find_element(By.ID, 'com.zappos.android.sixpmFlavor:id/welcome_text')
        text = login_text.text
        return text

    def favourites(self):
        self.driver.find_element(By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout[1]/android.widget.ListView/android.widget.LinearLayout[2]').click()
        self.driver.implicitly_wait(30)

    def find_favourites_text(self):
        fav_text = self.driver.find_element(By.ID, 'com.zappos.android.sixpmFlavor:id/list_name')
        text = fav_text.text
        return text







