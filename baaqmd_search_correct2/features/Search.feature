Feature: Search

@P1 @1
Scenario: Simple Search
Given I navigate to baaqmd main page
  When I perform search for "Climate" query
  Then I see relevant results returned for "Climate" query
  And I refine query on Search page and check the relevance of the result
  And I check the first card from the results