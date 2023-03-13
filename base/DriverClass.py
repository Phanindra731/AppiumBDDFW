from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_cap = {
            "appium:deviceName": "emulator-5554",
            "platformName": "android",
            "appium:platformVersion": "10",
            # "appium:automationName":'UiAutomator2',
            "appium:appPackage": "com.apalya.myplexmusic.sample",
            "appium:appActivity": "com.apalya.vimusic.musicsample.MyplexDemoActivity"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        return driver
