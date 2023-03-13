import allure
from allure_commons.types import AttachmentType
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common.exceptions import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.actions import interaction
from selenium.webdriver.common.actions.action_builder import ActionBuilder
from selenium.webdriver.common.actions.pointer_input import PointerInput
from selenium.webdriver.support.wait import WebDriverWait
import utilities.CustomLogger as cl
import time
from appium.webdriver.common.touch_action import TouchAction

class BasePage:
    log = cl.customLogger()
    x= "promod"

    def __init__(self, driver):
        self.driver = driver

    def waitForElement(self, locatorvalue, locatorType):
        locatorType = locatorType.lower()
        element = None

        wait = WebDriverWait(self.driver, 10, poll_frequency=1,
                             ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                 NoSuchElementException])
        if locatorType == "id":
            element = wait.until(lambda x: x.find_element_by_id(locatorvalue))
            return element
        elif locatorType == "class":
            element = wait.until(lambda x: x.find_element_by_class_name(locatorvalue))
            return element
        elif locatorType == "description":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator('UiSelector().description("%s")' % (locatorvalue)))
            return element
        elif locatorType == "index":
            element = wait.until(
                lambda x: x.find_element_by_android_uiautomator("UiSelector().index(%d)" % int(locatorvalue)))
            return element
        elif locatorType == "text":
            element = wait.until(lambda x: x.find_element_by_android_uiautomator('text("%s")' % locatorvalue))
            return element
        elif locatorType == "xpath":
            element = wait.until(lambda x: x.find_element_by_xpath('%s' % (locatorvalue)))
            return element
        elif locatorType == "css_selector":
            element = wait.until(lambda x: x.find_element_by_css_selector(locatorvalue))
            return element
        else:
            self.log.info("Locator value " + locatorvalue + "not found")

        return element

    def getElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.waitForElement(locatorValue, locatorType)
            self.log.info("Element found with LocatorType: " + locatorType + " with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Element not found with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False
        return element

    def clickElement(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.click()
            self.log.info(
                "Clicked on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to click on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False
        return element

    def sendText(self, text, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            element.send_keys(text)
            self.log.info(
                "Send text  on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
        except:
            self.log.info(
                "Unable to send text on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False

    def gettext(self, locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType).get_attribute("text")
            self.log.info(
                "Get text" + element + "on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            return element

        except:
            self.log.info(
                " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
            self.takeScreenshot(locatorType)


    def isDisplayed(self, locatorValue, locatorType="id"):
            element = None
            try:
                locatorType = locatorType.lower()
                element = self.getElement(locatorValue, locatorType)
                element.is_displayed()
                self.log.info(
                    " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + "is displayed ")
                return True
            except:
                self.log.info(
                    " Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue + " is not displayed")
                self.takeScreenshot(locatorType)
                #assert False
                return False


    def screenShot(self, screenshotName):
        fileName = screenshotName + "_" + (time.strftime("%d_%m_%y_%H_%M_%S")) + ".png"
        screenshotDirectory = "../screenshots/"
        screenshotPath = screenshotDirectory + fileName
        try:
            self.driver.save_screenshot(screenshotPath)
            self.log.info("Screenshot save to Path : " + screenshotPath)

        except:
            self.log.info("Unable to save Screenshot to the Path : " + screenshotPath)

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)

    def keyCode(self, value):
        self.driver.press_keycode(value)

    def scrollElement(self, locatorValue, locatorType):
        try:
            locatorType = locatorType.lower()
            wait = WebDriverWait(self.driver, 25, poll_frequency=1, ignored_exceptions=None)
            element = wait.until(lambda x: x.find_element_by_android_uiautomator
            ('new UiScrollable(new UiSelector()).scrollIntoView(%s("%s"))' % (locatorType,
                                                                              locatorValue)))
            element.click()

        except:
            self.log.info("Unable to scroll")

    def implicitwait(self, value):
        self.driver.implicitly_wait(value)

    def dragseekbar(self,dir,locatorValue, locatorType="id"):
        element = None
        try:
            locatorType = locatorType.lower()
            element = self.getElement(locatorValue, locatorType)
            print("Device Width and Height : ",self.driver.get_window_size())
             # out of print statement is :Device Width and Height :  {'width': 1440, 'height': 2621}
            deviceSize = self.driver.get_window_size()
            screenWidth = deviceSize['width']
            screenHeight = deviceSize['height']

            ######Right to Left#######
            startx = screenWidth*8.6/9
            endx = screenWidth/9
            starty = screenHeight/2
            endy = screenHeight/2
            ###### Left to Right    #######
            startx2 = screenWidth/9
            endx2 = screenWidth*8.6/9
            starty2 = screenHeight/2
            endy2 = screenHeight/2
            #obj = self.driver.find_element_by_id("com.vodafone.vodafoneplay:id/mediacontroller_progress")
            # strn1 = driver.find_element_by_id("com.vodafone.vodafoneplay:id/timeLL")
            # print(strn1.text)
            actions = TouchAction(self.driver)
            if dir == "Right to left":
                actions.long_press(element).move_to(None, endx, endy).release().perform()
            else:
                actions.long_press(element).move_to(None, endx2, endy2).release().perform()
        except:
            self.log.info(
                "Unable to drag on Element with LocatorType: " + locatorType + " and with the locatorValue :" + locatorValue)
            self.takeScreenshot(locatorType)
            assert False
        return element

    def scrollandclick(self,searchelement):
        # element = self.clickElement("//*[@text='Top Shows in Hindi']","xpath")
        # TouchAction(self.driver).press(x=570, y=565).move_to(x=570, y=200).release().perform()
        # self.scrollElement(self._shemaroocarousel,"xpath")
        # TouchAction(self.driver).press(x=570, y=565).move_to(x=570, y=200).release().perform()
        self.driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector().scrollable(true).instance(0)).scrollIntoView(new UiSelector().textContains("%s").instance(0))'%searchelement).click()
        time.sleep(2)
        # element = wait.until(lambda x: x.find_element_by_android_uiautomator
        # ('new UiScrollable(new UiSelector()).scrollIntoView(%s("%s"))' % (locatorType,
        #                                                                   locatorValue)))
    def swipetostart(self):
        # swipe(startX, startY, endX, endY, duration)
        #self.driver.swipe(893, 474, 893, 1422, 1000)actions = TouchAction(self.driver)

        #actions = TouchAction(self.driver)
        actions = ActionChains(self.driver)
        actions.w3c_actions = ActionBuilder(self.driver, mouse=PointerInput(interaction.POINTER_TOUCH, "touch"))
        actions.w3c_actions.pointer_action.move_to_location(893, 474)
        actions.w3c_actions.pointer_action.pointer_down()
        actions.w3c_actions.pointer_action.move_to_location(885, 1422)
        actions.w3c_actions.pointer_action.release()
        actions.perform()












