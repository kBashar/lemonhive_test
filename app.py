import json
import jsonschema
from flask import Flask, request, jsonify

from jsonschema.exceptions import ValidationError
from error.invalid import InvalidDataFormat


app = Flask(__name__)

@app.errorhandler(InvalidDataFormat)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

def get_config():
    return json.dumps({
    "firstName": "Khyrul",
    "secondName": "bashar",
    "ageInYears": 31,
    "address": "Dhaka",
    "creditScore": 89.3
})

def write_config(data):
    with open("mock_cloud/configuration-file.json") as f:
        # data_json = json.load(fp=f)
        # print(data_json)
        # data_json.append(data)
        print(data)
        json.dump(data, f)

def validate_data(data) -> bool: 
    """
    validates the input data against the schema.
    
    data: json data to validate

    returns: True, False.

    If the data is invalid the function returns `False`. otherwise returns `True`.
    """
    # Define the JSON schema
    schema = {
        "type": "object",
        "properties": {
            "firstName": {"type": "string"},
            "secondName": {"type": "string"},
            "ageInYears": {"type": "integer"},
            "address": {"type": "string"},
            "creditScore": {"type": "number"}
        },
        "required": ["firstName", "secondName", "ageInYears", "address", "creditScore"]
    }
    try:
        jsonschema.validate(data, schema)
        print("Data is valid.")
        return True
    except jsonschema.ValidationError as e:
        print("Data is invalid.")
        print(e)
        return False


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.get("/config")
def download_config():
    return get_config()

@app.post("/config")
def upload_config():
    data = request.get_json()
    print(data)
    if validate_data(data):
        # write_config(data)
        return data
    else:
        raise InvalidDataFormat("Data format Invalid", status_code=400)
