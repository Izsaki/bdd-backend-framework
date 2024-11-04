import pytest
from pytest_bdd import scenarios, given, when, parsers, then

from config.TestConfig import TestConfig
from utils.api.RestClient import RestClient

scenarios("../feature/rest_ageguesser.feature")
test_config = TestConfig()

def rest_client():
    if pytest.rest_client is None:
        print("ERROR - Rest Client is not set")
    else:
        return pytest.rest_client

@given("The REST API is set")
def set_up_rest():
    pytest.rest_client = RestClient(test_config.rest_base_url)

@when(parsers.parse('I get the result for name $"{name:l}"'), )
def get_age_for_name(name):
    response = rest_client().call(endpoint="", method="GET", params={"name":name}, data=None, json="None")
    pytest.response = response

@then(parsers.parse('The result should be $"{expected_age:d}"'),)
def check_expected_age(expected_age):
    if pytest.response.status_code != 200:
        assert("Unsuccesfull api call", pytest.response.status_code == 200)
    else:
        json = pytest.response.json()
        print("Response json: " + json.__str__())
        assert("The expected age should match with actual" , expected_age == json["age"])

