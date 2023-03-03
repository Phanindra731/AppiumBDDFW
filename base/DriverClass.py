from appium import webdriver


class Driver:
    def getDriverMethod(self):
        desired_cap = {
            "deviceName": "97cda28f",
            "platformName": "android",
            "platformVersion": "10",
            "appPackage": "com.apalya.myplexmusic.sample",
            "appActivity": "com.apalya.vimusic.musicsample.MyplexDemoActivity"
        }

        driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
        return driver
