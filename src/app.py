import json
import jsonschema
from pathlib import Path
from flask import Flask, request, jsonify, current_app
from .error.server_exception import ServerException




app = Flask(__name__)
app.config.update({
        "Defualt_Storage": "mock_cloud/configuration-file.json"
        })

@app.errorhandler(ServerException)
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
    try:
        storage = current_app.config.get("Defualt_Storage")
        
        filepath = Path(storage)
        # if there is no file, i.e. there was no upload. we return None.
        if not filepath.is_file():
            return None
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except Exception as e:
        return None

def create_config_file(storage_path):
    try:
        #create directories
        index_of_last_path_separator = storage_path.rfind("/")
        dirs = Path(storage_path[0:index_of_last_path_separator])
        dirs.mkdir(parents=True, exist_ok=True)
        # finally create file
        file_path = Path(storage_path)
        file_path.touch(exist_ok=True)
        return True
    except Exception as e:
        return False


def write_config(data):
    """
    Writes given data to a storage. 
    Currently it only supports local file storage.

    data: json data to write
    """
    storage_path = current_app.config.get("Defualt_Storage")
    print(storage_path)

    filepath = Path(storage_path)
    # if there is no file, let's create a file to store.
    if not filepath.is_file():
        create_config_file(storage_path)
    with open(filepath, "w") as f:
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
        return True
    except jsonschema.ValidationError as e:
        return False

@app.get("/config")
def download_config():
    current_app
    data = get_config()
    if not data:
        raise ServerException("No data Found", status_code=404)
    else:
        return data

@app.post("/config")
def upload_config():
    data = request.get_json()
    if validate_data(data):
        write_config(data)
        return {
            "message": "success"
        }
    else:
        raise ServerException("Data format Invalid", status_code=400)
