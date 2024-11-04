import pytest
from pytest_bdd import scenarios, given, when, then, parsers

from config.TestConfig import TestConfig

scenarios("../feature/dummy.feature")
dummy_expected = {"value": 10}
test_config = TestConfig()

#Fixture - runs before each test function that uses it
@pytest.fixture
def dummy_fixture():
    print("\n START ")
    #TODO put Some code here
    print("Dummy fixture run")
    yield
    print("TEARDOWN")
    #TODO put some code here
    #subprocess.run("allure generate allure-results")

#GIVEN
@given("The environment is set up")
def environment_setup(dummy_fixture):
    #TODO put some code here
    print("The environment is setting up")

#WHEN
@when("I send API call")
def send_api_call():
    #TODO put some lines of code here
    print("API call sending")

#THEN
@then(parsers.parse('the backed has a response and expected value of $"{actual_value:d}"'),)
def check_response(actual_value):
    #TODO put some lines of code here
    print("Checking response")
    dummy_actual = actual_value
    assert dummy_expected["value"] == dummy_actual