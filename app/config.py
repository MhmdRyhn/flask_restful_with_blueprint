from app import settings
from app.core.models import BaseModel
from app.utils import get_module_from_dotted_path

MODELS_MODULE_NAME = 'models'


def _get_pynamodb_models():
    classes = []
    for blueprint in settings.BLUEPRINTS:
        models_module_path = f'{blueprint}.{MODELS_MODULE_NAME}'
        module = get_module_from_dotted_path(models_module_path)
        for attribute_name in dir(module):
            attribute = getattr(module, attribute_name)
            if isinstance(attribute, type) and issubclass(attribute, BaseModel) and attribute is not BaseModel:
                classes.append(attribute)
    return classes


def create_resources():
    classes = _get_pynamodb_models()
    for klass in classes:
        klass.create_table(wait=True)


if __name__ == '__main__':
    create_resources()
