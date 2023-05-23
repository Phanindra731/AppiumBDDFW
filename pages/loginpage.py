import time

from base.BasePage import BasePage
import utilities.CustomLogger as cl

class loginpage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    #locaters
    _userid = "//android.widget.EditText[@index=0]" #xpath
    _mobilenumber = "//*[@text='mobile']" #xpath
    _contentid = "//*[@text='Content Id(optional)']" #xpath
    _launchbtn = "//*[@text='Launch']"  #xpath
    _setasdeafult = "//*[@text='Set As Default OFF']" #xpath
    _deeplinklaunchwithsong = "//*[@text='Launch with song']"  #xpath
    _deeplinklaunchwithvideo = "//*[@text='Launch with Video']" #xpath
    _deeplinklaunchwithplaylist = "//*[@text='Launch with Playlist']" #xpath
    _deeplinklaunchwithtopchart = "//*[@text='Launch with TopChart']" #xpath
    _deeplinklaunchwithpodcast = "//*[@text='Launch with Podcast']" #xpath
    _deeplinklaunchwithartist = "//*[@text='Launch with Artist']" #xpath
    _deeplinklaunchwithalbum = "//*[@text='Launch with Album']" #xpath
    _deeplinklaunchwithevent = "//*[@text='Launch with Event']" #xpath
    _deeplinklaunchwithpodcastalbum = "//*[@text='Launch with Podcast Album']"#xpath
    _deeplinklaunchwithbucket = "//*[@text='Launch with Bucket']"#xpath
    _deeplinklaunchwithsearch = "//*[@text='Launch with Open Search']"#xpath
    _deeplinklaunchwithmymusic = "//*[@text='Launch with Open My Music']"#xpath
    _hungamaheader = "com.apalya.myplexmusic.sample:id/ivLogo"  #id
    _errorpage = "com.apalya.myplexmusic.sample:id/tvErrorTitle"  #id
    _appversionheader = "com.apalya.myplexmusic.sample:id/tvAppVersion" #id
    _changeenv ="com.apalya.myplexmusic.sample:id/spinnerEnv" #id
    _stagenv = "//*[@text='Staging']"  #xpath
    _changeenvbtn = "com.apalya.myplexmusic.sample:id/btnSaveEnv" #id
    _newuserpopup ="com.apalya.myplexmusic.sample:id/recyclerView" #id
    _maybelater = "//*[@text='maybe later']"  #xpath
    _Continuewithads ="//*[@text='Continue With Ads']" #xpath

    def verifyreturnuserpopup(self):
        self.waitForElement(self._newuserpopup,"id")
        e1 = self.isDisplayed(self._newuserpopup,"id")
        self.waitForElement(self._Continuewithads,"xpath")
        e2 = self.isDisplayed(self._Continuewithads,"xpath")
        if (e1 & e2):
            cl.allureLogs("Return user popup displayed")
            print("Wellcome popup displayed")
            assert True
        else:
            assert False

    def verifynewuserpopup(self):
        self.waitForElement(self._newuserpopup,"id")
        e1 = self.isDisplayed(self._newuserpopup,"id")
        self.waitForElement(self._maybelater,"xpath")
        e2 = self.isDisplayed(self._maybelater,"xpath")
        if (e1 & e2):
            print("Wellcome popup displayed")
            assert True
        else:
            assert False

    def changeappenvtostagging(self):
        for i in range(0,6):
            self.clickElement(self._appversionheader,"id")
        self.scrollandclick("Production")
        #time.sleep(5)
        #self.scrollElement(self._changeenv,"id")
        #self.waitForElement(self._changeenv,"id")
        #self.clickElement(self._changeenv,"id")
        self.clickElement(self._stagenv,"xpath")
        self.clickElement(self._changeenvbtn,"id")
        #t1=self.gettext(self._stagenv,"xpath")
       # cl.allureLogs("App  environment changed to " + t1)
        self.swipetostart()
        self.swipetostart()
        self.swipetostart()
  #      self.scrollandclick("Launch")




    def verifyheader(self):
        self.waitForElement(self._hungamaheader,"id")
        e = self.isDisplayed(self._hungamaheader,"id")
        if e:
            cl.allureLogs("Succssfully launchhed in music home page")
        else:
            assert False
    def verifyerrorpage(self):
        self.waitForElement(self._errorpage, "id")
        e = self.isDisplayed(self._errorpage, "id")
        if e:
            e1=self.gettext(self._errorpage, "id")
            cl.allureLogs("Diplayed error page " + e1)
        else:
            assert False
    def enteruserid(self,user_id):
        self.sendText(user_id,self._userid,"xpath")
        cl.allureLogs("entered user id"+ user_id)

    def entermobilenumber(self,mobile_number):
        self.sendText(mobile_number,self._mobilenumber,"xpath")
        cl.allureLogs("entered user id"+ mobile_number)

    def contentid(self,conntent_id):
        self.sendText(conntent_id,self._contentid,"xpath")
        cl.allureLogs("entered user id"+ conntent_id)

    def clicklaunchbtn(self):
        self.clickElement(self._launchbtn,"xpath")
        cl.allureLogs("clicked on launch button")

    def clickonsetdefaultbtn(self):
        self.clickElement(self._setasdeafult,"xpath")
        cl.allureLogs("Clicked on set as default button")

    def clickonlaunchwithsong(self):
        self.clickElement(self._deeplinklaunchwithsong,"xpath")
        cl.allureLogs("click on launch_with_song deeplink")

    def clickonlaunchwithvideo(self):
        self.clickElement(self._deeplinklaunchwithvideo,"xpath")
        cl.allureLogs("click on launch_with_video deeplink")

    def clickonlaunchwithplaylist(self):
        self.clickElement(self._deeplinklaunchwithplaylist,"xpath")
        cl.allureLogs("click on launch_with_playlist deeplink")

    def clickonlaunchwittopchart(self):
        self.clickElement(self._deeplinklaunchwithtopchart,"xpath")
        cl.allureLogs("click on launch_with_topchart deeplink")

    def clickonlaunchwithpodcast(self):
        self.clickElement(self._deeplinklaunchwithpodcast,"xpath")
        cl.allureLogs("click on launch_with_video podcast")


    def clickonlaunchwithartist(self):
        self.clickElement(self._deeplinklaunchwithartist,"xpath")
        cl.allureLogs("click on launch_with_artist deeplink")

    def clickonlaunchwithalbum(self):
        self.clickElement(self._deeplinklaunchwithalbum,"xpath")
        cl.allureLogs("click on launch_with_album deeplink")


