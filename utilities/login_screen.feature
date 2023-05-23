# This is a Feature file

Feature: Launch the app
@tagt1 @sanity
    Scenario Outline: login using valid cradentials

      Given create class object
      Then enter mobile number<mobilenumber>
      Then click on launch
      Then verify the launch
      Examples:
        | mobilenumber |
      |9581794876    |
      |9492156669    |
@tagt1 @sanity
  Scenario Outline: login with non vi number

      Given create class object
      Then enter mobile number<nonvinumber>
      Then click on launch
      Then verify the error should dsiplay
    Examples:
      | nonvinumber |
    |9581992218   |
@tagt1 @sanity
  Scenario Outline: login with invalidnumber

      Given create class object
      Then enter mobile number<invalidnummber>
      Then click on launch
    Examples:
      | invalidnummber |
  |95819922        |

  @tagt1 @sanity
  Scenario Outline: verify new user popup

      Given create class object

      Then enter new user mobile number<mobilenumber>
      #Then change app enivironment to stagging
      Then click on launch
      Then verify the new user popup
      Examples:
        | mobilenumber |
      |8886682956    |

@tagt0 @sanity
  Scenario Outline: verify return user popup

      Given create class object
      Then enter return user mobile number<mobilenumber>
      Then change app enivironment to stagging
      Then click on launch
      Then verify the return user popup
      Examples:
        | mobilenumber |
      |9010234707    |







