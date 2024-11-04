import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from config.TestConfig import TestConfig
from utils.api.SoapClient import SoapClient

scenarios("../feature/soap_calculator.feature")
test_config = TestConfig()

def soap_client():
    if pytest.soap_client is None:
        print("ERROR - SOAP Client is not set")
    else:
        return pytest.soap_client

@given(parsers.parse('The soap API is set with the WSDL'),)
def set_up_api_by_wsdl():
    wsdl_path = test_config.wsdl
    print("WSDL path is: " + wsdl_path)
    pytest.soap_client = SoapClient(wsdl_path)

@when(parsers.parse('The Addition method is called with $"{num1:d}" and $"{num2:d}"'),)
def call_addition(num1, num2):
    pytest.add_value = soap_client().call_add(num1, num2)
    print(pytest.add_value)

@then(parsers.parse('The result should be $"{expected:d}"'),)
def then_call(expected):
    assert pytest.add_value == expected
