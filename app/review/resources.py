import flask_restful
import webargs
from webargs.flaskparser import use_args, use_kwargs

from app.review.blueprint import API
from app.review.models import ReviewModel
from app.review.schemas import ReviewSchema
from app.log import logger


@API.resource('/books/<string:product_id>', strict_slashes=False, methods=['GET', 'PUT', 'DELETE'],
              endpoint='book-review')
@API.resource('/books', strict_slashes=False, methods=['POST'], endpoint='add-book-review')
class ReviewResource(flask_restful.Resource):
    serializer = ReviewSchema
    model = ReviewModel

    @use_args(ReviewSchema)
    def post(self, args):
        data = dict(
            product_id=str(args['product_id']),
            user_id=str(args['user_id']),
            review_text=str(args['review_text'])
        )

        review_obj = self.model.dict2model(data)
        try:
            review_obj.save()
        except Exception as ex:
            logger.error(ex)
            raise

        return self.serializer().dump(data), 201

    @use_kwargs({'product_id': webargs.fields.UUID()})
    def get(self, **kwargs):
        try:
            review_obj = self.model.get(hash_key=str(kwargs['product_id']))
        except self.model.DoesNotExist as ex:
            logger.error(str(ex))
            response = {
                'msg': 'resource with product id {} does not exist'.format(kwargs['product_id'])
            }
            return response, 404
        return self.serializer().dump(review_obj), 200
