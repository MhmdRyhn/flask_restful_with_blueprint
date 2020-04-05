from pynamodb import attributes

from app.settings import DYNAMODB_CONFIG
from app.core.models import BaseModel


class ReviewModel(BaseModel):
    product_id = attributes.UnicodeAttribute(hash_key=True)
    user_id = attributes.UnicodeAttribute()
    review_text = attributes.UnicodeAttribute()

    class Meta(BaseModel.Meta):
        table_name = f"{DYNAMODB_CONFIG.get('env', 'local')}-product-review"
