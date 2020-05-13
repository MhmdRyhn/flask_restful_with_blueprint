import flask

from app import settings, log
from app.config import create_resources
from app.utils import get_module_from_dotted_path


def _create_app():
    app = flask.Flask(settings.APP_NAME)
    app.logger.addHandler(log.stream_log_handler())
    app.logger.addHandler(log.file_log_handler())

    for blueprint in settings.BLUEPRINTS:
        module = get_module_from_dotted_path(blueprint)
        blueprint_obj = getattr(module, 'blueprint')
        url_prefix = getattr(module, 'url_prefix')
        app.register_blueprint(blueprint_obj, url_prefix=url_prefix)

    @app.errorhandler(Exception)
    def handle_exception(exception):
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


def _debug(host='localhost', port=5000, debug=True):
    flask_app = _create_app()
    flask_app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    create_resources()
    _debug()
