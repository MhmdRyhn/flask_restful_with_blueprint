import flask
import flask_restful

blueprint = flask.Blueprint('review', __name__)
url_prefix = '/review'

API = flask_restful.Api(blueprint)
