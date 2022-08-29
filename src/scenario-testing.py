from wsgiref import headers
import schemathesis
import yaml
from hypothesis.stateful import initialize
import requests

with open('src/scenario.yaml') as file:
    scenarioConfig = yaml.full_load(file)
BASE_URL = scenarioConfig['BASE_URL']
ENDPOINT = scenarioConfig['ENDPOINT']
JSONBODY = scenarioConfig['BODY']

schema = schemathesis.from_uri(BASE_URL, validate_schema=False)
BaseAPIWorkflow = schema.as_state_machine()

class APIWorkflow(BaseAPIWorkflow):
    authHeader: dict
    def setup(self):
        response = requests.post(
            "http://127.0.0.1:8000/api/v1/"+ENDPOINT[0], json=JSONBODY
        )
        token = response.json()["auth_token"]
        self.headers = {"Authorization": f"Bearer {token}"}

    def get_call_kwargs(self, case):
        return {"headers": self.headers}
    
    # @schema.parametrize()
    # def custom_test1(case):
    #     response = case.call()
    #     case.call_and_validate(response,headers=APIWorkflow.authHeader)

    # def check_condition(response, case):
    #     ""

    # def validate_response(self, response, case):
    #     super().validate_response(response, case, additional_checks=(self.check_condition,))

    
