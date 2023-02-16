from flask import jsonify

class InvalidDataFormat(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        # schema = {
        #     "firstName": str,
        #     "secondName": str,
        #     "ageInYears": int,
        #     "address": str,
        #     "creditScore": float
        # } 
        # __payload = f'Data should be of this format {str(schema)}'
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv