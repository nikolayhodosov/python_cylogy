Feature: Search

@P1 @1
Scenario: Simple Search
Given I navigate to STA SMS Form page
  When I fill telephone number in phone field
  Then I click Submit button
  And I see Successfull message about SMS Form Submit