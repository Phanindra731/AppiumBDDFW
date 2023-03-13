import time

from base.BasePage import BasePage
import utilities.CustomLogger as cl

class HomePage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

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
            e1 = self.isDisplayed(self._podcastquicktab, "id")
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







