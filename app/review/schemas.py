from marshmallow import fields

from app.core.schemas import BaseSchema


class ReviewSchema(BaseSchema):
    product_id = fields.UUID(required=True)
    user_id = fields.UUID(required=True)
    review_text = fields.Str(required=True)
