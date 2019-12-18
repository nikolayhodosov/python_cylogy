Feature: Search

@P1 @1
Scenario: Simple Search
Given I navigate to baaqmd main page
  When I perform search for "nikolay" query
  Then I perform search for "pleasechange" query2
  And I click Login button
  And I click Content Editor button from Launchpad
  And I perform search for "{2B892399-8AFD-469E-B27D-2F33FF51647B}" id1
  And I click Send SMS button in Air District Tools tab
  And I click Continue button in the SMS Message popup
  And I see relevant results returned for "Climate" query
  And I refine query on Search page and check the relevance of the result
  And I check the first card from the results