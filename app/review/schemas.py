from marshmallow import fields

from app.core.schemas import BaseSchema


class ReviewSchema(BaseSchema):
    review_id = fields.UUID(required=True, dump_only=True)
    review_text = fields.Str(required=True)
