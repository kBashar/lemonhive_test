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
    """
    Retrives the json data from the storage.
    Currently it fetches data from local storage. 

    returns a json data
    """
    with open("mock_cloud/configuration-file.json", "r") as f:
        data = json.load(f)
        return data

def write_config(data):
    """
    Writes given data to a storage. 
    Currently it only supports local file storage.

    data: json data to write
    """
    with open("mock_cloud/configuration-file.json", "w") as f:
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
        write_config(data)
        return data
    else:
        raise InvalidDataFormat("Data format Invalid", status_code=400)
