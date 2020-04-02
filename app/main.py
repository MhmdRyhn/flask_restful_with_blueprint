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
    return app


def _debug(host='localhost', port=5000, debug=True):
    flask_app = _create_app()
    flask_app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    _debug()
