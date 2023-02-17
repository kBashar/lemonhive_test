### Run the Project
1. Create a python virtual environment using `venv` module.
   ```
   $ python39 -m venv <env name>
   ```
2. Activate the virtual env.
3. Clone the repository.  
   ```
   $ git clone https://github.com/kBashar/lemonhive_test.git
   ```
4. Install dependencies.
    ```
    $ pip install -r requirements.txt
    ```
### 5.Run the development Server
To run the development server from project root directory (lemonhive_test) 
1. set environment variable `FLASK_APP` to `src.app:app`
2. Windows: `set FLASK_APP=src.app:app`
3. Unix: `export FLASK_APP=src.app:app`

### Endpoints

#### /config [GET]
returns a json formated data blob.
This endpoint returns **status 404** if there is no storage found.
```json
{
    "message": "No data Found"
}
```

#### /config [POST]
Accepts json data. json schema is as follows:  
```json
    {
        "firstName": str,
        "secondName": str,
        "ageInYears": int,
        "address": str,
        "creditScore": float
    }
```  
If valid a success message is sent back.  
```json
    {
        "message": "success"
    }
```
If POSTed data is invalid the endpoint will return error **status 400**.
```json
    {
        "message":"Data format Invalid"
    }
```

### Run tests
To run tests inside the root directory simplyrun
```bash
    $ pytest
```

### Schema Verification  
We use `jsonschema` library for json data validation. 
Upon getting a POST request in `/config` route, data is validated in 
`validate_data` function. This function depends on `jsonchema` library to
validate a json data input. 
If the data is invalid the library raises a `ValidationError` exception. And the function
returns `False`. Else if there is no error the function return `True`.