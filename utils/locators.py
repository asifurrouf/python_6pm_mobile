from appium import webdriver
from selenium.webdriver.common.by import By

class HomePageLocators(object):
    SEARCH_BOX = (By.XPATH, 'com.zappos.android.sixpmFlavor:id/menu_search')
    SEARCH_TEXT = (By.XPATH, '/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.view.ViewGroup/android.widget.TextView[1]')