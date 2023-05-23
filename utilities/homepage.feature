@sanity
Feature: Testing home page
@tagt1
    Scenario: verify home page quick tabs
      Given Launch the music app
      Then verify playlist quick tab
      Then verify Charts quick tab
      Then verify Podcast quick tab
      Then verify MusicVideo quick tab
@tagt1
    Scenario: verify home page Bottem tabs
        Given Launch the music app
        Then verify VI Home tab
        Then verify Music tab
        Then verify Search tab
        Then verify My Music tab
@tagt1
    Scenario: verify topbanners and header
        Given Launch the music app
        Then verify hungama header
        Then verify topbanners
@tagt1 @tagt4
    Scenario: verify playlist quick tab
        Given Launch the music app
        Then click on Playlist quick tab
        Then verify playlist listing page
@tagt1 @tagt4
    Scenario: verify playlist detailpage
        Given Launch the music app
        Then click on Playlist quick tab
        Then verify playlist listing page
        Then click on any playlist content
        Then verify playlist detailpage for header and count
        Then verify playlist deatailpage for share button
        Then verify playlist deatailpage for CTA add to playlist
        Then verify playlist detailpage for CTA add to favourite
        Then verify playlist detailpage for CTA download
        Then verify playlist detailpage for CTA Play
        Then verify Playlist thumbnail image
        Then verify playlist detailpage backbutton
@tagt1 @tagt4
    Scenario: verify playlist detailpage kebab menu
        Given Launch the music app
        Then click on Playlist quick tab
        Then verify playlist listing page
        Then click on any playlist content
        Then click on kebab menu
        Then verify kebab menu option close button
        Then click on kebab menu
        Then verify kebab menu option add to queue
        Then verify kebab menu option add to playlist
        Then verify kebab menu option show album
        Then verify kebab menu option download song
        Then verify kebab menu option share

@tagt1
     Scenario: verify Charts quick tab
        Given Launch the music app
        Then click on charts quick tab
        Then verify charts listing page
@tagt1
  Scenario: verify charts detailpage
        Given Launch the music app
        Then click on charts quick tab
        Then click on any playlist content
        Then verify playlist detailpage for header and count
        Then verify playlist deatailpage for share button
        Then verify playlist deatailpage for CTA add to playlist
        Then verify playlist detailpage for CTA add to favourite
        Then verify playlist detailpage for CTA download
        Then verify playlist detailpage for CTA Play
        Then verify Playlist thumbnail image
        Then verify playlist detailpage backbutton
@tagt1
    Scenario: verify charts detailpage kebab menu
       Given Launch the music app
       Then click on charts quick tab
       Then verify charts listing page
       Then click on any playlist content
       Then click on kebab menu
       Then verify kebab menu option close button
       Then click on kebab menu
       Then verify kebab menu option add to queue
       Then verify kebab menu option add to playlist
       Then verify kebab menu option show album
       Then verify kebab menu option download song
       Then verify kebab menu option share
@tagt1
  Scenario: verify Podcast quick tab
           Given Launch the music app
           When click on Podcast quick tab
           Then verify Podcast quick tab

  @tagt1
  Scenario: verify Podcast detailpage
        Given Launch the music app
        When click on Podcast quick tab
        Then click on any playlist content
        Then verify Podcast detailpage for title and sub title
        Then verify Podcast detailpage for share button
        Then verify Podcast detailpage for CTA add to favourite
       Then verify Podcast detailpage for CTA Play
        Then verify Podcast detail page thumbnail image
       Then verify Podcast detail page backbutton
         Then verify podcast detail page About the podcast header
         Then verify podcast detail page About the podcast discription
         Then verify podcast detail page episodes list


    Scenario: verify Podcast detailpage kebab menu
       Given Launch the music app
       When click on Podcast quick tab
       Then click on any playlist content
       Then click on podcast detailapge kebab menu
       Then verify podcast detailapge kebab menu option play next
       Then verify podcast detailapge kebab menu option add to queue
       Then verify podcast detailapge kebab menu option download episode
       Then verify podcast detailapge kebab menu option share
       Then verify podcast detailpage kebab menu close button
@tagttest
   Scenario: verify Music Video quick tab
           Given Launch the music app
           When click on Music videos quick tab
           Then verify Music videos listing page
