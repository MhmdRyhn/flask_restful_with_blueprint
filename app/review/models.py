from pynamodb import attributes

from app import settings
from app.core.models import BaseModel


class ReviewModel(BaseModel):
    product_id = attributes.UnicodeAttribute(hash_key=True)
    review_text = attributes.UnicodeAttribute()

    class Meta(BaseModel.Meta):
        # table_name = f"{settings.DYNAMODB_CONFIG.get('env', 'local')}-product-review"
        table_name = 'dev-dummy-2'
