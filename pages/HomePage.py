import time

from appium.webdriver.common.appiumby import AppiumBy

from base.BasePage import BasePage
import utilities.CustomLogger as cl
import unittest


class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    log = cl.customLogger()
    # locaters
    _playlistquicktab = "com.apalya.myplexmusic.sample:id/layoutActionPlaylists"  #id
    _chartsquicktab = "com.apalya.myplexmusic.sample:id/layoutActionCharts"   #id
    _podcastquicktab = "com.apalya.myplexmusic.sample:id/layoutActionPodcast"    #id
    _musicvideoquicktab ="com.apalya.myplexmusic.sample:id/layoutActionVideoPlaylist"  #id
    _topbanners = "com.apalya.myplexmusic.sample:id/ivSliderBanner"  #id
    _vihometab = "com.apalya.myplexmusic.sample:id/layoutViHome" #id
    _musichometab ="com.apalya.myplexmusic.sample:id/layoutHomeNew"  #id
    _searchtab ="com.apalya.myplexmusic.sample:id/layoutSearchNew"  #id
    _mymusictab = "com.apalya.myplexmusic.sample:id/layoutMyMusicNew" #id
    _hungamaheader = "com.apalya.myplexmusic.sample:id/ivLogo" #id
    _recentlyplayedcarousel = "//*[@text='Recently Played']" #xpath
    _weeklychartscarousel = "//*[@text='Weekly Charts']"  #xpath
    _newsongscarousel = "//*[@text='New Songs']"   #xpath
    _popularplaylistcarousel ="//*[@text='Popular Playlists']"  #xpath
    _citytoppercarousel = "//*[@text='City Topper']"  #xpath
    _listingpageheadertitle = "com.apalya.myplexmusic.sample:id/tvToolbarTitle"   #id
    _playlistdetailpageheader = "com.apalya.myplexmusic.sample:id/tv_song_title_playlist"  #id
    _podcastdetailpageheader = "com.apalya.myplexmusic.sample:id/tv_podcast_title"  #id
    _podcastdetailpagecount = "com.apalya.myplexmusic.sample:id/tv_podcast_subtitle"  #id
    _podcastdetailpage_favourite = "com.apalya.myplexmusic.sample:id/tv_podcast_fav"  #id
    _podcastdetailpage_share = "com.apalya.myplexmusic.sample:id/iv_share_podcast"  #id
    _podcastdetailpage_playbtn = "com.apalya.myplexmusic.sample:id/tv_podcast_play"  #id
    _podcastdetailpage_episodeslist =  "com.apalya.myplexmusic.sample:id/rl_podcast_scrollable_layout"  #id
    _podcastdetailpage_aboutpodcattext = "com.apalya.myplexmusic.sample:id/tv_about_podcast"  #id
    _podcastdetailpage_textdiscriiption = "com.apalya.myplexmusic.sample:id/tv_about_podcast_description" #id
    _podcastdetailpage_thumbnail = "com.apalya.myplexmusic.sample:id/iv_poster_image_podcast"  #id
    _podcastdetailpage_backbutton = "com.apalya.myplexmusic.sample:id/iv_podcast_back" #id
    _podcastdetailpage_keabmenu = "com.apalya.myplexmusic.sample:id/podcast_more_vert"  #id
    _podcastdetailpagekebabmenu_playnext = "com.apalya.myplexmusic.sample:id/play_next" #id
    _podcastdetailpagekebabmenu_addtoqueue = "com.apalya.myplexmusic.sample:id/add_to_queue_play" #id
    _podcastdetailpagekebabmenu_downloadepisode = "com.apalya.myplexmusic.sample:id/download_episode" #id
    _podcastdetailpagekebabmenu_share = "com.apalya.myplexmusic.sample:id/share_podcast" #id
    _podcastdetailpagekebabmenu_close = "com.apalya.myplexmusic.sample:id/close_menu"  #id

    _playlistlistingcontent = "//androidx.recyclerview.widget.RecyclerView/android.widget.LinearLayout[1]/android.widget.TextView" #xpath
    _sharebuttonin_ply_lst = "com.apalya.myplexmusic.sample:id/iv_share_playlist"  #id
    _Playlistcount = "com.apalya.myplexmusic.sample:id/tv_playlist_subtitle"  #id
    _playlistbackbutton = "com.apalya.myplexmusic.sample:id/tv_playlist_subtitle" #id
    _CTAaddtoplaylist = "com.apalya.myplexmusic.sample:id/iv_add_to_playlist"   #id
    _CTAaddtofavourite = "com.apalya.myplexmusic.sample:id/iv_playlist_favourite"  #id
    _CTAdownloadplaylist = "com.apalya.myplexmusic.sample:id/iv_playlist_download"  #id
    _CTAplaybuttonplylst = "com.apalya.myplexmusic.sample:id/rl_play_action" #id
    _playlistthumbnail = "com.apalya.myplexmusic.sample:id/iv_poster_image_playlist"  #id
    _addtoqueue = "com.apalya.myplexmusic.sample:id/rl_add_to_queue"  #id
    _addtoplaylist = "com.apalya.myplexmusic.sample:id/rl_add_to_playlist"  #id
    _showalbum = "com.apalya.myplexmusic.sample:id/rl_show_album"  #id
    _downloadsong ="com.apalya.myplexmusic.sample:id/rl_download_song_layout"  #id
    _share = "com.apalya.myplexmusic.sample:id/rl_share_song_layout"  #id
    _closekebab = "com.apalya.myplexmusic.sample:id/close_menu"  #id

    def verifypodcastdetailpage_kebab(self):
        try:

            l1=self.driver.find_elements(AppiumBy.ID,self._podcastdetailpage_keabmenu)

            self.log.info("element found with locator" + self._podcastdetailpage_keabmenu)
            self.waitForElement(self._podcastdetailpage_keabmenu,"id")
            l1[0].click()
            time.sleep(1)
            #self.waitForElement(_kebab,"id")
            self.takeScreenshot("kebab menu")
            cl.allureLogs("CLicked on kebab menu in podcast detail page" )
        except:
            self.log.info("element not found with locator" + self._podcastdetailpage_keabmenu)
            assert False


    def verifypodcastkebabmenuoption_close(self):
        e1 = self.isDisplayed(self._podcastdetailpagekebabmenu_close, "id")

        if e1:
            t1 = self.gettext(self._podcastdetailpagekebabmenu_close, "id")
            cl.allureLogs(t1 + " button dislayed")
        else:
            cl.allureLogs("close button is not displayed")
            assert False

    def verifypodcastkebabmenuoption_playnext(self):
        e1 = self.isDisplayed(self._podcastdetailpagekebabmenu_playnext, "id")

        if e1:
            t1 = self.gettext(self._podcastdetailpagekebabmenu_playnext, "id")
            cl.allureLogs(t1 + " button dislayed")
        else:
            cl.allureLogs("play next button is not displayed")
            assert False
    def verifypodcastkebabmenuoption_downloadepisode(self):
        e1 = self.isDisplayed(self._podcastdetailpagekebabmenu_downloadepisode, "id")

        if e1:
            t1 = self.gettext(self._podcastdetailpagekebabmenu_downloadepisode, "id")
            cl.allureLogs(t1 + " button dislayed")
        else:
            cl.allureLogs("downloadepisode button is not displayed")
            assert False

    def verifypodcastkebabmenuoption_addtoqueue(self):
        e1 = self.isDisplayed(self._podcastdetailpagekebabmenu_addtoqueue, "id")

        if e1:
            t1 = self.gettext(self._podcastdetailpagekebabmenu_addtoqueue, "id")
            cl.allureLogs(t1 + " button dislayed")
        else:
            cl.allureLogs("downloadepisode button is not displayed")
            assert False

    def verifypodcastkebabmenuoption_share(self):
        e1 = self.isDisplayed(self._podcastdetailpagekebabmenu_share, "id")

        if e1:
            t1 = self.gettext(self._podcastdetailpagekebabmenu_share, "id")
            cl.allureLogs(t1 + "share button dislayed")
        else:
            cl.allureLogs("share button is not displayed")
            assert False

    def verifykebabmenuoption_share(self):
        e1 = self.isDisplayed(self._share, "id")

        if e1:
            t1 = self.gettext(self._share, "id")
            cl.allureLogs(t1 + "share button dislayed")
        else:
            cl.allureLogs("share button is not displayed")
            assert False


    def verifykebabmenuoption_showalbum(self):
        e1 = self.isDisplayed(self._showalbum, "id")

        if e1:
            t1 = self.gettext(self._showalbum, "id")
            cl.allureLogs(t1 + "button displayed")
        else:
            cl.allureLogs("show album button is not displayed")
            assert False


    def verifykebabmenuoption_downloadsong(self):
        e1 = self.isDisplayed(self._downloadsong, "id")

        if e1:
            t1 = self.gettext(self._downloadsong, "id")
            cl.allureLogs(t1 + "button displayed")
        else:
            cl.allureLogs("downloadsong button is not displayed")
            assert False



    def verifykebabmenu_addtoplylst(self):
        e1 = self.isDisplayed(self._addtoplaylist, "id")

        if e1:
            t1 = self.gettext(self._addtoplaylist, "id")
            cl.allureLogs(t1 + "button displayed")
        else:
            cl.allureLogs("add to playlist button is not displayed")
            assert False


    def  verifykebabmenuaddtoqueue(self):
        e1 = self.isDisplayed(self._addtoqueue,"id")

        if e1:
            t1 = self.gettext(self._addtoqueue,"id")
            cl.allureLogs(t1 + "button displayed")
        else:
            cl.allureLogs("add to queue button is not displayed")
            assert False


    def verifykebabclosebtn(self):
        e1 = self.isDisplayed(self._closekebab,"id")

        if e1:
            cl.allureLogs("Kebab menu Close button displayed")
            self.clickElement(self._closekebab,"id")
            _kebab = "com.apalya.myplexmusic.sample:id/iv_playlist_more_vert"
            l1 = self.driver.find_elements(AppiumBy.ID, _kebab)
            d1=l1[0].is_displayed()
            if d1:
                cl.allureLogs("kebab menu close button is verified(workingfine)")
            else:
                cl.allureLogs("kebab menu close button is  not working")
                assert False

        else:
            cl.allureLogs("Kebab menu Close button not displayed")
            assert False


    def plylstkebab(self):
        try:
            _kebab ="com.apalya.myplexmusic.sample:id/iv_playlist_more_vert"
            l1=self.driver.find_elements(AppiumBy.ID,_kebab)
            self.log.info("element found with locator" + _kebab)
            self.waitForElement(_kebab,"id")
            l1[0].click()
            time.sleep(1)
            #self.waitForElement(_kebab,"id")
            self.takeScreenshot("kebab menu")
            cl.allureLogs("CLicked on kebab menu in playlist detail page" )
        except:
            self.log.info("element not found with locator" + _kebab)
            assert False

    def verifyplaylistbackbutton(self):
        e1 = self.isDisplayed(self._playlistbackbutton, "id")
        if e1:
            cl.allureLogs("Playlist detail page back button displayed")
        else:
            cl.allureLogs("Playlist detail page back button not displayed")
            assert False

    def verifyplaylistthumnail(self):
        e1 = self.isDisplayed(self._playlistthumbnail, "id")
        if e1:
            cl.allureLogs("Playlist Thumnail image displayed")
        else:
            cl.allureLogs("Playlist Thumnail image not displayed")
            assert False

    def verifyCTAplayforplylst(self):
        e1=  self.isDisplayed(self._CTAdownloadplaylist,"id")
        if e1:
            cl.allureLogs("CTA Play displayed")
        else:
            cl.allureLogs("CTA Play not displayed")
            assert False

    def verifyCTAdownloadplylist(self):
        e1=  self.isDisplayed(self._CTAdownloadplaylist,"id")
        if e1:
            cl.allureLogs("CTA download playlist displayed")
        else:
            cl.allureLogs("CTA download playlist not displayed")
            assert False

    def verifyaddtofavourite(self):
        e1=  self.isDisplayed(self._CTAaddtofavourite,"id")
        if e1:
            cl.allureLogs("CTA add to favourite displayed")
        else:
            cl.allureLogs("CTA add to favourite not displayed")
            assert False

    def verifyaddtoplylst(self):
        e1=  self.isDisplayed(self._CTAaddtoplaylist,"id")
        if e1:
            cl.allureLogs("CTA add to playlist displayed")
        else:
            cl.allureLogs("CTA add to playlist not displayed")
            assert False
    def verifyplylst_headerandcount(self):
       e1 = self.isDisplayed(self._playlistdetailpageheader,"id")
       e2 = self.isDisplayed(self._Playlistcount,"id")
       if e1 & e2:
           cl.allureLogs("Playlist Title and Count displayed")
       else:
           cl.allureLogs("Playlist Title and Count not displayed")
           assert False
    def verifyplylstdetailsharebtn(self):
        e1 = self.isDisplayed(self._sharebuttonin_ply_lst,"id")
        if e1:
            cl.allureLogs("Share button displayed")
        else:
            cl.allureLogs("share button not displayed")
            assert False


    def clickonplaylistcontent(self):
        self.waitForElement(self._playlistlistingcontent, "xpath")
        self.clickElement(self._playlistlistingcontent, "xpath")
        e3 = self.isDisplayed(self._listingpageheadertitle, "id")
        if e3:
            cl.allureLogs("Playlist opened")
        else:
            cl.allureLogs("Playlist not opened")
            assert False


        # e1 = self.gettext(self._playlistlistingcontent,"id")
        # print(e1)

        # e2 =  self.gettext(self._listingpageheadertitle,"id")
        # print(e2)
        # if e1==e2:
        #     cl.allureLogs("Playlist opened")
        # else:
        #     cl.allureLogs("Playlist not opened")
        #     assert False


    def clickonplaylistquicktab(self):
        self.clickElement(self._playlistquicktab,"id")
        cl.allureLogs("Clicked on Playlistquick tab")

    def verifyplaylistlistingpage(self):
        e1 = self.gettext(self._listingpageheadertitle,"id")
        if e1 == "Playlists":
            cl.allureLogs("Playlist listinng page opened")
        else:
            cl.allureLogs("instead of playlist" + e1 + "Opened")
            assert False

    def verify_chartslistlistingpage(self):
        e1 = self.gettext(self._listingpageheadertitle,"id")
        if e1 == "Charts":
            cl.allureLogs("Charts listinng page opened")
        else:
            cl.allureLogs("instead of Charts" + e1 + "Opened")
            assert False

    def clickchartsquicktab(self):
        self.waitForElement(self._chartsquicktab,"id")
        self.clickElement(self._chartsquicktab,"id")
        cl.allureLogs("Clicked on charts quick tab")

    def verifychartslistingpage(self):
        e1 = self.gettext(self._listingpageheadertitle,"id")
        if e1 == "Charts":
            cl.allureLogs("Charts listinng page opened")
        else:
            cl.allureLogs("instead of Charts" + e1 + "Opened")
            assert False

    def clickpodcastquicktab(self):
        self.clickElement(self._podcastquicktab,"id")
        cl.allureLogs("Clicked on podcast QUICK TAB ")

    def verifypodcastlistingpage(self):
        e1 = self.gettext(self._listingpageheadertitle,"id")
        if e1 == "Podcasts":
            cl.allureLogs("Podcasts listinng page opened")
        else:
            cl.allureLogs("instead of Podcasts" + e1 + "Opened")
            assert False

    def verifypodcatdetailpage_headerandcount(self):
        e1 = self.isDisplayed(self._podcastdetailpageheader, "id")
        t1 = self.gettext(self._podcastdetailpageheader, "id")
        e2 = self.isDisplayed(self._podcastdetailpagecount, "id")
        t2 = self.gettext(self._podcastdetailpagecount, "id")
        if e1 & e2:
            cl.allureLogs(t1 +" Podcast Title and sub title displayed " + t2)
        else:
            cl.allureLogs("Podcast Title and Count not displayed")
            assert False
    def verifypodcatdetailpage_share(self):
        try :
            self.isDisplayed(self._podcastdetailpage_share,"id")
            cl.allureLogs("CTA share Displayed")

        except:
            print("Playlist quick tab ot found")
            cl.allureLogs("CTA share not displayed")
            assert False
    def verifypodcatdetailpage_addtofavourite(self):
        try :
            self.isDisplayed(self._podcastdetailpage_favourite,"id")
            t1 = self.gettext(self._podcastdetailpage_favourite,"id")
            cl.allureLogs(t1 + " CTA Displayed")

        except:
            cl.allureLogs("CTA not displayed")
            assert False
    def verifypodcatdetailpage_play(self):
        try :
            self.isDisplayed(self._podcastdetailpage_playbtn,"id")
            t1 = self.gettext(self._podcastdetailpage_playbtn,"id")
            cl.allureLogs(t1 + " CTA Displayed")

        except:
            cl.allureLogs("CTA not displayed")
            assert False
    def verifypodcatdetailpage_aboutpodcast(self):
        try :
            self.isDisplayed(self._podcastdetailpage_aboutpodcattext,"id")
            t1 = self.gettext(self._podcastdetailpage_aboutpodcattext,"id")
            cl.allureLogs(t1 + " header Displayed")

        except:
            cl.allureLogs(" about the podcast header not displayed")
            assert False
    def verifypodcatdetailpage_aboutpodcasttext(self):
        try :
            self.isDisplayed(self._podcastdetailpage_textdiscriiption,"id")
            t1 = self.gettext(self._podcastdetailpage_textdiscriiption,"id")
            cl.allureLogs(t1 + " Displayed")

        except:
            cl.allureLogs(" about the podcast text not displayed")
            assert False
    def verifypodcatdetailpage_episodeslist(self):
        try :
            self.isDisplayed(self._podcastdetailpage_episodeslist,"id")
            #t1 = self.gettext(self._podcastdetailpage_textdiscriiption,"id")
            cl.allureLogs("Episodes scrollable layout Displayed")

        except:
            cl.allureLogs("Episodes not displayed")
            assert False
    def verifypodcatdetailpage_thumbnail(self):
        try :
            self.isDisplayed(self._podcastdetailpage_thumbnail,"id")
            #t1 = self.gettext(self._podcastdetailpage_textdiscriiption,"id")
            cl.allureLogs("Detail page thumbnail Displayed")

        except:
            cl.allureLogs("Detail page thumbnail not displayed")
            assert False
    def verifypodcatdetailpage_backbutton(self):
        try :
            self.isDisplayed(self._podcastdetailpage_backbutton,"id")
            #t1 = self.gettext(self._podcastdetailpage_textdiscriiption,"id")
            cl.allureLogs("Detail page back button Displayed")

        except:
            cl.allureLogs("Detail page back button not displayed")
            assert False

    def clickmusicvideoquicktab(self):
        self.clickElement(self._musicvideoquicktab,"id")

    def verifymusicvideolistingpage(self):
        e1 = self.gettext(self._listingpageheadertitle,"id")
        if e1 == "Music Videos":
            cl.allureLogs("Music Videos listinng page opened")
        else:
            cl.allureLogs("instead of Music Videos" + e1 + "Opened")
            assert False



    def VerifyPlaylistQuickTabs(self):
        try :

            e1 = self.isDisplayed(self._playlistquicktab,"id")
            cl.allureLogs("Playlist quick tab Displayed")

        except:
            print("Playlist quick tab ot found")
            cl.allureLogs("Playlist quick tab not displayed")
            assert False

    def Verifychartsquicktab(self):
        try:
            e1 = self.isDisplayed(self._chartsquicktab, "id")
            cl.allureLogs("Charts quick tab Displayed")

        except:
            print("Charts quick tab ot found")
            cl.allureLogs("Charts quick tab not displayed")
            assert False

    def Verifypodcastquicktab(self):
        try:
            self.isDisplayed(self._podcastquicktab, "id")
            cl.allureLogs("podacst quick tab Displayed")

        except:
            print("Podcast quick tab ot found")
            cl.allureLogs("poodacst quick tab not displayed")
            assert False

    def Verifymusicvideoquicktab(self):
        try:
            e1 = self.isDisplayed(self._musicvideoquicktab, "id")
            cl.allureLogs("Music Video quick tab Displayed")

        except:
            print("Music Video quick tab ot found")
            cl.allureLogs("Music Video  quick tab not displayed")
            assert False

    def Verifyvihometab(self):
        try:
            e1 = self.isDisplayed(self._vihometab, "id")
            cl.allureLogs("VI Home tab Displayed")

        except:
            print("VI Home tab not found")
            cl.allureLogs("VI Home tab not displayed")
            assert False

    def Verifymusichometab(self):
        try:
            e1 = self.isDisplayed(self._musichometab, "id")
            cl.allureLogs("Music Home tab Displayed")

        except:
            print("Music Home tab not found")
            cl.allureLogs("Music Home tab not displayed")
            assert False

    def VerifySearchtab(self):
        try:
            e1 = self.isDisplayed(self._searchtab, "id")
            cl.allureLogs("Search tab Displayed")

        except:
            print("Search tab not found")
            cl.allureLogs("Search tab not displayed")
            assert False

    def VerifyMymusictab(self):
        try:
            e1 = self.isDisplayed(self._mymusictab, "id")
            cl.allureLogs("My Music tab Displayed")

        except:
            print("My Music  tab not found")
            cl.allureLogs("My Music tab not displayed")
            assert False

    def Verifytopbanner(self):
        try:
            e1 = self.isDisplayed(self._topbanners, "id")
            cl.allureLogs("Top banners Displayed")

        except:
            print("Top banners not found")
            cl.allureLogs("Top banners not displayed")
            assert False

    def Verifyhungamaheader(self):
        try:
            e1 = self.isDisplayed(self._hungamaheader, "id")
            cl.allureLogs("Hungama header Displayed")

        except:
            print("Hungama header not found")
            cl.allureLogs("Hungama header not displayed")
            assert False







