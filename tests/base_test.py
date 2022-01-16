from appium import webdriver
from appium.webdriver.common.mobileby import By
import allure

@allure.severity(allure.severity_level.CRITICAL)
class BaseTest:

    def setUp(self):
        desired_cap = {
            "appium:deviceName": "0123456789ABCDEF",
            "platformName": "Android",
            "appium:app": "C:/Users/FoysalAhmed/Desktop/QUPS_assigmnets/6pm_android/6PM_v2.1.1.apk"
        }

        driver = webdriver.Remote("http://127.0.0.1:4723/wd/hub", desired_cap)




