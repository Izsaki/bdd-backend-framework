from zeep import Client

class SoapClient:

    def __init__(self, wsdl_path):
        self.wsdl = wsdl_path
        self.client = Client(wsdl=self.wsdl)

    def call_add(self, num1: int, num2: int) -> int:
        return self.client.service.Add(num1, num2)

    def call_subtract(self, num1: int, num2: int) -> int:
        return self.client.service.Substract(num1, num2)
