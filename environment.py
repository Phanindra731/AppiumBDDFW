
import time
from behave import step
from base.BasePage import BasePage
from base.DriverClass import Driver
import utilities.CustomLogger as cl
import configurationfiles.DeviceConfig as dc
from behave.contrib.scenario_autoretry import patch_scenario_with_autoretry
log = cl.customLogger()


def before_scenario(context, scenario):
    log.info("Automation Started")
    context.testVariable = "This is a Test variable"
    context.driver1 = Driver
    context.driver = context.driver1.getDriverMethod(context)
    context.bp = BasePage(context.driver)
    #context.bp.launchWebPage(dc.url, dc.title)
    # for scenario in feature.scenarios:
    #     if "smoke_test" in scenario.effective_tags:
    #         patch_scenario_with_autoretry(scenario, max_attempts=3)


def after_scenario(context, scenario):
    #time.sleep(1)
    context.driver.quit()
    #log.info("Automation Ended")
