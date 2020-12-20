import requests
from os.path import join, dirname
from jsonschema import validate
import json

def test_post_headers_body_json():
    url = "https://ghibliapi.herokuapp.com/vehicles/"
    headers = {'Content-Type': 'application/json'}

    response = requests.request("GET", url, headers=headers)

    schema = load_schema('main_schema.json')
    validate(response.json(), schema)
    assert response.status_code == 200

    for i in range(len(response.json())):
        child_url = response.json()[i]['url']
        test_assertion_schema(child_url, headers)

def test_assertion_schema(url, headers):
    response = requests.request("GET", url=url, headers=headers)
    assert response.status_code == 200

def load_schema(file_name):
    relative_path = join('json_schema', file_name)
    absolute_path = join(dirname(__file__), relative_path)

    with open(absolute_path) as schema_file:
        return json.loads(schema_file.read())
