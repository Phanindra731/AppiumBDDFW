from behave import given, when, then
import utilities.CustomLogger as cl
from pages.loginpage import loginpage
from pages.HomePage import HomePage
from base.BasePage import BasePage
import configurationfiles.DeviceConfig as dc
class HomePageTest:
    @given(u'create class object')
    def classObject(context):
        context.lp = loginpage(context.driver)
        context.bp = BasePage(context.driver)
        context.hp = HomePage(context.driver)
        print("App launched")
        cl.allureLogs("app launched")

    @given(u'Launch the music app')
    def classObject(context):
        context.lp = loginpage(context.driver)
        context.bp = BasePage(context.driver)
        context.hp = HomePage(context.driver)
        print("App launched")
        cl.allureLogs("app launched")
        context.lp.entermobilenumber(dc.number)
        context.lp.clicklaunchbtn()

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

    @then(u'click on Playlist quick tab')
    def clickplaylisttab(context):
        context.hp.clickonplaylistquicktab()
    @then(u'verify playlist listing page')
    def verifyplaylist(context):
        context.hp.verifyplaylistlistingpage()

    @then(u'click on any playlist content')
    def clickonplaylistcontent(context):
        context.hp.clickonplaylistcontent()

    @then(u'verify playlist detailpage for header and count')
    def verifyheaderandcount(context):
        context.hp.verifyplylst_headerandcount()
    @then(u'verify playlist deatailpage for share button')
    def verifysharebutton(context):
        context.hp.verifyplylstdetailsharebtn()
    @then(u'verify playlist deatailpage for CTA add to playlist')
    def verifyaddtoplaylist(context):
        context.hp.verifyaddtoplylst()
    @then(u'verify playlist detailpage for CTA add to favourite')
    def verifyaddtofavourite(context):
        context.hp.verifyaddtofavourite()
    @then(u'verify playlist detailpage for CTA download')
    def verifydownloadcta(context):
        context.hp.verifyCTAdownloadplylist()
    @then(u'verify playlist detailpage for CTA Play')
    def verifyCTAplay(context):
        context.hp.verifyCTAplayforplylst()
    @then(u'verify Playlist thumbnail image')
    def verifyplaylistthumbnail(context):
        context.hp.verifyplaylistthumnail()
    @then(u'verify playlist detailpage backbutton')
    def verifybackbutton(context):
        context.hp.verifyplaylistbackbutton()

    @then(u'click on kebab menu')
    def clickonkebabmenuinplylst(context):
        context.hp.plylstkebab()

    @then(u'verify kebab menu option close button')
    def verifykebabmenuclosebtn(context):
        context.hp.verifykebabclosebtn()
    @then(u'verify kebab menu option add to queue')
    def verifykebabmenuoption_addtoqueue(context):
        context.hp.verifykebabmenuaddtoqueue()

    @then(u'verify kebab menu option add to playlist')
    def verifykebabmenuoption_addtoplaylist(context):
        context.hp.verifykebabmenu_addtoplylst()

    @then(u'verify kebab menu option show album')
    def verifykebabmenuoption_showalbum(context):
        context.hp.verifykebabmenuoption_showalbum()

    @then(u'verify kebab menu option download song')
    def verifykebabmenuoption_downloadsong(context):
        context.hp.verifykebabmenuoption_downloadsong()

    @then(u'verify kebab menu option share')
    def verifykebabmenuoption_share(context):
        context.hp.verifykebabmenuoption_share()

    @then(u'click on charts quick tab')
    def clickon_chartsquicktab(context):
        context.hp.clickchartsquicktab()

    @then(u'verify charts listing page')
    def verify_chartslistingpage(context):
        context.hp.verify_chartslistlistingpage()


    # @then(u'verify charts listing page')
    # def verifychartslistingpage(context):
    #     context.hp.verifychartslistingpage()

    @when(u'click on Podcast quick tab')
    def click_podcastquicktab(context):
        context.hp.clickpodcastquicktab()

    @then(u'verify Podcast detailpage for title and sub title')
    def verifychartslistingpage(context):
        context.hp.verifypodcatdetailpage_headerandcount()

    @then(u'verify Podcast detailpage for share button')
    def verifypodcastdetailpage_share(context):
        context.hp.verifypodcatdetailpage_share()

    @then(u'verify Podcast detailpage for CTA add to favourite')
    def verifypodcastdetailpage_Addtofavourite(context):
        context.hp.verifypodcatdetailpage_addtofavourite()

    @then(u'verify Podcast detailpage for CTA Play')
    def verifypodcastdetailpage_CTAPLAY(context):
        context.hp.verifypodcatdetailpage_play()

    @then(u'verify Podcast detail page thumbnail image')
    def verifypodcastdetailpage_thumbnail(context):
        context.hp.verifypodcatdetailpage_thumbnail()

    @then(u'verify Podcast detail page backbutton')
    def verifypodcastdetailpage_Backbutton(context):
        context.hp.verifypodcatdetailpage_backbutton()

    @then(u'verify podcast detail page About the podcast header')
    def verifypodcastdetailpage_aboutpodcast(context):
        context.hp.verifypodcatdetailpage_aboutpodcast()

    @then(u'verify podcast detail page About the podcast discription')
    def verifypodcastdetailpage_aboutpodcastdiscription(context):
        context.hp.verifypodcatdetailpage_aboutpodcasttext()

    @then(u'verify podcast detail page episodes list')
    def verifypodcastdetailpage_episodeslist(context):
        context.hp.verifypodcatdetailpage_episodeslist()

    @then(u'click on podcast detailapge kebab menu')
    def verifypodcastdetailpage_kebabmenu(context):
        context.hp.verifypodcastdetailpage_kebab()

    @then(u'verify podcast detailapge kebab menu option play next')
    def verifypodcastdetailpagekebabmenu_playnext(context):
        context.hp.verifypodcastkebabmenuoption_playnext()

    @then(u'verify podcast detailapge kebab menu option add to queue')
    def verifypodcastdetailpagekebabmenu_addtoqueue(context):
        context.hp.verifypodcastkebabmenuoption_addtoqueue()

    @then(u'verify podcast detailapge kebab menu option download episode')
    def verifypodcastdetailpagekebabmenu_downloadepisode(context):
        context.hp.verifypodcastkebabmenuoption_downloadepisode()

    @then(u'verify podcast detailapge kebab menu option share')
    def verifypodcastdetailpagekebabmenu_share(context):
        context.hp.verifypodcastkebabmenuoption_share()

    @then(u'verify podcast detailpage kebab menu close button')
    def verifypodcastdetailpagekebabmenu_close(context):
        context.hp.verifypodcastkebabmenuoption_close()

    @when(u'click on Music videos quick tab')
    def clickmusicvideosquicktab(context):
        context.hp.clickmusicvideoquicktab()

    @then(u'verify Music Video quick tab')
    def verifymusicvideoslistingpage(context):
        context.hp.verifymusicvideolistingpage()