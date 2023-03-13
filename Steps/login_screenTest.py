from behave import given, when, then
import utilities.CustomLogger as cl
from pages.loginpage import loginpage
from base.BasePage import BasePage

class login_screenTest:

    # @given(u'create class object')
    # def classObject(context):
    #     context.lp = loginpage(context.driver)
    #     context.bp = BasePage(context.driver )
    #     print("App launched")
    #     cl.allureLogs("app launched")

    @then(u'enter mobile number{mobilenumber}')
    def step_clickonloginbtn(context,mobilenumber):
        #context.mb = mobilenumber
        context.lp.entermobilenumber(mobilenumber)

    @then(u'click on launch')
    def clickLaunch(context):
        context.lp.clicklaunchbtn()

    @then(u'verify the launch')
    def verifyapplaunch(context):
        context.lp.verifyheader()

    @then(u'verify the error should dsiplay')
    def verifyerrorpage(context):
        context.lp.verifyerrorpage()
    @then(u'change app enivironment to stagging')
    def changetheappenv(context):
        context.lp.changeappenvtostagging()

    @then(u'verify the new user popup')
    def verifywelcomepopup(context):
        context.lp.verifynewuserpopup()

    @then(u'enter return user mobile number{mobilenumber}')
    def enterreturnusermobileno(context,mobilenumber):
        context.lp.entermobilenumber(mobilenumber)

    @then(u'enter new user mobile number{mobilenumber}')
    def enternewusermobileno(context, mobilenumber):
        context.lp.entermobilenumber(mobilenumber)


    @then(u'verify the return user popup')
    def verifywelcomepopup(context):
        context.lp.verifyreturnuserpopup()