
import time
from behave import step
from base.BasePage import BasePage
from base.DriverClass import Driver
import utilities.CustomLogger as cl
import configurationfiles.DeviceConfig as dc

log = cl.customLogger()


def before_all(context):
    log.info("Automation Started")
    context.testVariable = "This is a Test variable"
    context.driver1 = Driver
    context.driver = context.driver1.getDriverMethod(context)
    context.bp = BasePage(context.driver)
    #context.bp.launchWebPage(dc.url, dc.title)


def after_all(context):
    time.sleep(5)
    #context.driver.quit()
    #log.info("Automation Ended")
