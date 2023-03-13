from behave import given, when, then
import utilities.CustomLogger as cl
from pages.loginpage import loginpage
from pages.HomePage import HomePage
from base.BasePage import BasePage

class HomePageTest:
    @given(u'create class object')
    def classObject(context):
        context.lp = loginpage(context.driver)
        context.bp = BasePage(context.driver)
        context.hp = HomePage(context.driver)
        print("App launched")
        cl.allureLogs("app launched")
    @then(u'verify playlist quick tab')
    def verifyplaylistquicktab(context):
        context.hp.VerifyPlaylistQuickTabs()

    @then(u'verify Charts quick tab')
    def verifychartsquicktab(context):
        context.hp.Verifychartsquicktab()

    @then(u'verify Podcast quick tab')
    def verifypoddcastquicktab(context):
        context.hp.Verifypodcastquicktab()

    @then(u'verify MusicVideo quick tab')
    def verifymusicquicktab(context):
        context.hp.Verifymusicvideoquicktab()

    @then(u'verify VI Home tab')
    def verifyVIhometab(context):
        context.hp.Verifyvihometab()
    @then(u'verify Music tab')
    def verifyMusictab(context):
        context.hp.Verifymusichometab()
    @then(u'verify Search tab')
    def verifySearch(context):
        context.hp.VerifySearchtab()
    @then(u'verify My Music tab')
    def verifyMymsictab(context):
        context.hp.VerifyMymusictab()
    @then(u'verify hungama header')
    def verifyhungamaheader(context):
        context.hp.Verifyhungamaheader()
    @then(u'verify topbanners')
    def verifytopbanners(context):
        context.hp.Verifytopbanner()