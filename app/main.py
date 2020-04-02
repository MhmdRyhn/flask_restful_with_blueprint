from importlib import import_module

import flask

from app import settings


def _create_app():
    app = flask.Flask(__name__)
    for blueprint in settings.BLUEPRINTS:
        module = import_module(blueprint)
        blueprint_obj = getattr(module, 'blueprint')
        url_prefix = getattr(module, 'url_prefix')
        app.register_blueprint(blueprint_obj, url_prefix=url_prefix)

    @app.errorhandler(Exception)
    def handle_exception(exception):
        print(dir(exception))
        return flask.jsonify(error_code=500, error_message=str(exception)), 500

    @app.errorhandler(404)
    def not_found_error(error):
        return flask.jsonify(error_code=error.code, error_message=str(error)), error.code

    @app.errorhandler(400)
    @app.errorhandler(422)
    def handle_error(error):
        headers = error.data.get("headers", None)
        messages = error.data.get("messages", ["Invalid request."])
        if headers:
            return flask.jsonify({'error_code': error.code, "error_message": messages}), error.code, headers
        return flask.jsonify({'error_code': error.code, "error_message": messages}), error.code

    @app.errorhandler(500)
    def not_found_error(error):
        return flask.jsonify(error_code=error.code, error_message=str(error)), error.code

    return app


def _debug(host='localhost', port=5050, debug=True):
    flask_app = _create_app()
    flask_app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    _debug()
