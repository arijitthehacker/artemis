import schemathesis
import yaml

with open('src/scenario.yaml') as file:
    scenarioConfig = yaml.full_load(file)
BASE_URL = scenarioConfig['BASE_URL']
ENDPOINT = scenarioConfig['ENDPOINT']
print(BASE_URL)
print(ENDPOINT)
schema = schemathesis.from_uri(BASE_URL, validate_schema=False)