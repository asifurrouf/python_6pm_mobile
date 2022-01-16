from appium import webdriver
from selenium.webdriver.common import keys
import allure
import pytest
from appium.webdriver.common.touch_action import TouchAction
import time
from appium.webdriver.common.mobileby import By
from selenium.webdriver.common.keys import Keys

desired_cap = {
    "appium:deviceName": "0123456789ABCDEF",
    "platformName": "Android",
    "appium:app": "C:/Users/FoysalAhmed/Desktop/QUPS_assigmnets/6pm_android/6PM_v2.1.1.apk"
}

driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)
driver.implicitly_wait(50)
search_box = driver.find_element(By.ID,'com.zappos.android.sixpmFlavor:id/menu_search')
search_box.click()

driver.implicitly_wait(20)
search_box_type = driver.find_element(By.ID, 'com.zappos.android.sixpmFlavor:id/search_src_text')
# search_box_type.clear()
search_box_type.send_keys('shirts')
# search_box_type.send_keys(Keys.RETURN)