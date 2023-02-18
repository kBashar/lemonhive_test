import pytest
import json
from src.app import app as api_app
from flask import g

@pytest.fixture()
def app(tmpdir):
    app = api_app
    app.config.update({
        "TESTING": True,
        "Default_Storage": "test_mock_cloud/configuration-file.json"
    })


    # other setup can go here

    yield app

    # clean up / reset resources here

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture(scope="function")
def test_data():
    return {
        "firstName": "Nur",
        "secondName": "Alom",
        "ageInYears": 34,
        "address": "Dhaka",
        "creditScore": 93.9
    }

# first we test if Not Found 404 works

def test_config_get_not_found(client):
    """
        returns a 404 code if the `GET` request cannot find the file in cloud storage
    """
    response = client.get("/config")
    assert response.status_code == 404
    assert response.json["message"] == "No data Found"

def test_config_post(client, test_data):
    """
        Test to upload JSON data to cloud storage after validating the input data.
    """
    
    response = client.post("/config", json=test_data, headers={"Content-Type": "application/json"})
    assert response.status_code == 200
    assert response.json["message"] == "success"

def test_config_post_invalid_format(client, test_data):
    """
       The web service must return a 400 code if the `POST` 
       request JSON does not match the schema.

       We change creditScore object a string type. As schema declares it to be
       a number/float, it is an invalid data format. 400 status should be returned.

    """
    #change data type
    test_data["creditScore"] = "93.9"
    response = client.post("/config", json=test_data, headers={"Content-Type": "application/json"})
    assert response.status_code == 400
    assert response.json["message"] == "Data format Invalid"

def test_config_get(client, test_data):
    """
        Test to download JSON data to cloud storage after validating the input data.
    """
    response = client.get("/config")
    assert response.status_code == 200
    assert response.json == test_data