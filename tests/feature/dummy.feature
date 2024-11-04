@dummy_tag
Feature: Dummy
  Dummy Test for framework development

  @dummy_scenario_tag
  Scenario: Dummy Test
    Given The environment is set up
    When I send API call
    Then the backed has a response and expected value of $"10"

