from http import HTTPStatus
from flask import Flask
from flask import make_response, jsonify
from flask_cors import CORS
from jsonschema import ValidationError

from blueprints.feed.api import feed_blueprint


def create_app():
    _app = Flask(__name__)
    CORS(_app, resources={r"/feed-service/*": {"origins": "*"}})

    @_app.route('/are_you_alive')
    def are_you_alive():
        return make_response({"message": "Hello from service"}, HTTPStatus.OK)

    @_app.errorhandler(500)
    def internal_server_error(error):
        return make_response({"message": error.description}, HTTPStatus.INTERNAL_SERVER_ERROR)

    @_app.errorhandler(404)
    def not_found_error(error):
        return make_response({"message": error.description}, HTTPStatus.NOT_FOUND)

    @_app.errorhandler(400)
    def not_found_error(error):
        if isinstance(error.description, ValidationError):
            original_error = error.description
            return make_response(jsonify({'error': original_error.message}), HTTPStatus.BAD_REQUEST)

        return make_response({"message": error.description}, HTTPStatus.BAD_REQUEST)

    # resister the blueprints.
    _app.register_blueprint(feed_blueprint, url_prefix='/feed')

    return _app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port="8011")
