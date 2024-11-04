import json
import os

configfile_name = "config.json"
script_dir = os.path.dirname(__file__)
config_path = os.path.normpath(os.path.join(script_dir, '..', 'config', configfile_name))

class TestConfig:
    wsdl: str
    rest_base_url: str
    frontend_url: str

    def __init__(self):
        self.load()

    def load(self):
        json_data = json.load(open(config_path))
        self.wsdl = json_data["wsdlUrl"]
        self.rest_base_url = json_data["restBaseUrl"]
        self.frontend_url = json_data["frontendUrl"]

