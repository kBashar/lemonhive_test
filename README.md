## Install python


### Schema Verification  
We use `jsonschema` library for json data validation. 
Upon getting a POST request in `/config` route, data is validated in 
`validate_data` function. This function depends on `jsonchema` library to
validate a json data input. 
If the data is invalid the library raises a `ValidationError` exception. And the function
returns `False`. Else if there is no error the function return `True`.