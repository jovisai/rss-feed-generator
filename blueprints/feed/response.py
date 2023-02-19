from flask import make_response


class ApiResponse:
    def __init__(self, http_status_code, data='', error=False):
        self.http_status_code = http_status_code
        self.error = error
        if error:
            # in case of error, the data is usually a string message.
            self.message = data
        else:
            # when no error, data may be some object
            self.data = data
