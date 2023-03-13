Feature: Testing home page

    Scenario Outline: verify home page quick tabs

      Given create class object
      Then enter mobile number<mobilenumber>
      Then click on launch
      Then verify the launch
      Then verify playlist quick tab
      Then verify Charts quick tab
      Then verify Podcast quick tab
      Then verify MusicVideo quick tab

      Examples:
        | mobilenumber |
      |9581794876    |

  Scenario Outline: verify home page Bottem tabs

      Given create class object
      Then enter mobile number<mobilenumber>
      Then click on launch
      Then verify the launch
      Then verify VI Home tab
      Then verify Music tab
      Then verify Search tab
      Then verify My Music tab

      Examples:
        | mobilenumber |
      |9581794876    |
@tagt1
  Scenario Outline: verify topbanners and header

      Given create class object
      Then enter mobile number<mobilenumber>
      Then click on launch
      Then verify the launch
      Then verify hungama header
      Then verify topbanners

      Examples:
        | mobilenumber |
      |9581794876    |
