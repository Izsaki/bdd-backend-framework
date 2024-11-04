@api @rest
Feature: REST based age guesser
  There is an open Api that guess the age from name

  @age
  Scenario: Test Name for age
    Given The REST API is set
    When I get the result for name $"Lujza"
    Then The result should be $"50"
