## Install python


### Schema Verification  
We use `jsonschema` library for json data validation. 
Upon getting a POST request in `/config` route, data is validated in 
`validate_data` function. This function depends on `jsonchema` library to
validate a json data input. 
If the data is invalid the library raises a `ValidationError` exception. And the function
returns `False`. Else if there is no error the function return `True`.

### Run the development Server
To run the development server from project root directory (lemonhive_test) 
1. set environment variable `FLASK_APP` to `src.app:app`
2. Windows: `set FLASK_APP=src.app:app`
3. Unix: `export FLASK_APP=src.app:app`