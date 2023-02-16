# leomnhive_test

This document outlines a technical test for candidates seeking employment at Lemon Hive as a Full Stack or Backend developer.

This test will use the Python programming language and the following main packages:

* [`flask`](https://flask.palletsprojects.com/en/2.2.x/) - For creating web services
* [`pytest`](https://docs.pytest.org/en/7.1.x/) - For testing functionality
* [`venv`](https://docs.python.org/3/library/venv.html) - For isolating libraries from the system site directories
* [`google-cloud-storage`](https://pypi.org/project/google-cloud-storage/) - For interacting with the Google Cloud Storage API

You are not limited to using only these packages. You are free to install additional dependencies as you see fit, however you must make sure to adhere to the requirements detailed below.

## Scope

For this assessment we want you to create a simple upload/download service that provides a single endpoint, `/config` that accepts `GET` and `POST` requests. 

The expected behaviour of the endpoints are as follows:

* `GET`: Retrieves the JSON data inside a file named `configuration-file.json` from a Google Cloud storage bucket named `stored-configuration-files`
* `POST`: Uploads JSON data into a file named `configuration-file.json` to a Google Cloud storage bucket named `stored-configuration-files`. The contents of the JSON data should be verified to ensure they match the [JSON schema](#json-schema)

### Outputs

The following outputs are expected:

* A simple web service for uploading and downloading a JSON file to a Google Cloud storage bucket
* A test suite that verifies the main functionality of the web service. The acceptance test should check that we can upload a JSON and then retrieve the same JSON information from cloud storage

These outputs should be stored in a publicly available GitHub repository.

## Requirements

* The code must use Python 3.9
* The code must install without requiring additional libraries in the system site directories
* Any dependencies should be installed in a virtual environment via a `requirements.txt` file
* The web service must be written using `flask`
* The web service must run locally and must accept requests sent via `curl` or Postman to `localhost`
* The web service must accept JSON data (e.g. `data:application/json`), not file data
* The web service must return a 400 code if the `POST` request JSON does not match the schema 
* The web service must return a 404 code if the `GET` request cannot find the file in cloud storage
* The test suite must be written using `pytest`
* The test suite must pass without any additional action from the user beyond initialising the virtual environment
* The finished code must be placed in a publicly accessible GitHub repository

The following things are NOT expected of you during this assessment:

* You do not need to provide a UI for uploading the JSON file
* You do not need to provide the cloud storage bucket for hosting the JSON files
* You do not need to add authentication to the endpoints
* You do not need to provide credentials for the Google Cloud API - you should use mocks to execute your tests

### JSON Schema

The `POST` method for the `/config` endpoint should verify that the JSON data matches the following format:

```json
{
    "firstName": str,
    "secondName": str,
    "ageInYears": int,
    "address": str,
    "creditScore": float
}
```

## Scoring

The assessment will be evaluated based on the following criteria:

* Does the submission meet the requirements?
* Is the code understandable?
* Does the code make use of best practices? Such as: type hinting, docstrings, appropriate variable names, seperation of concerns, etc.
