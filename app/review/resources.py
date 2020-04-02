import uuid

import flask_restful
from webargs.flaskparser import use_args

from app.review.blueprint import API
from app.review.schemas import ReviewSchema


@API.resource('/books/<string:review_id>', strict_slashes=False, methods=['GET', 'PUT', 'DELETE'],
              endpoint='book-review')
@API.resource('/books', strict_slashes=False, methods=['POST'], endpoint='add-book-review')
class ReviewResource(flask_restful.Resource):
    serializer = ReviewSchema

    @use_args(ReviewSchema)
    def post(self, args):
        data = dict(
            review_id=str(uuid.uuid4()),
            review_text=args['review_text']
        )
        return self.serializer().dump(data), 201
