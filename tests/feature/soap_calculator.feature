@soap @backend
Feature: SOAP Calculator test
  There is an open SOAP Api Calculator to be tested

  @addition
  Scenario: Test Addition
    Given The soap API is set with the WSDL
    When The Addition method is called with $"5" and $"10"
    Then The result should be $"15"