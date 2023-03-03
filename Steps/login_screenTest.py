from behave import given, when, then
import utilities.CustomLogger as cl
from pages.loginpage import loginpage
from base.BasePage import BasePage

class login_screenTest:

    @given(u'create class object')
    def classObject(context):
        context.lp = loginpage(context.driver)
        context.bp = BasePage(context.driver )
        print("App launched")
        cl.allureLogs("app launched")

    @then(u'enter mobile number{mobilenumber}')
    def step_clickonloginbtn(context,mobilenumber):
        context.mb = mobilenumber
        context.lp.entermobilenumber(context.mb)

    @then(u'click on launch')
    def clickLaunch(context):
        context.lp.clicklaunchbtn()


    @when("Enter UserID")
    def methodTwo(context):
        print("L2 - Enter the UserID in Login Screen")


    @when("Enter password")
    def methodThree(context):
        print("L3 - Enter the Password in Login Screen")


    @when("Click on Login Button")
    def methodFour(context):
        print("L4 - Clicked on the login Button")


    @when("Home page opens")
    def methodFour(context):
        print("L5 - Home Page opened")


    @then("Verify Home Screen")
    def methodFive(context):
        print("L6 - Home Screen Opened")


    @then("Take Screenshot")
    def methodSix(context):
        print("L7 - ScreenShot taken")
