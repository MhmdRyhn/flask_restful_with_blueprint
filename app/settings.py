APP_NAME = 'flask-restful-logging'

BLUEPRINTS = [
    'app.review',
]

# Logging
LOG_FILE_PATH = '../log-info.log'

LOG_FORMATTER_STRING = (
    '%(asctime)s - [%(levelname)s] - %(message)s\n'
    '[File] - %(pathname)s\n'
    '[Function/Class] - %(funcName)s [Line No.] - %(lineno)d\n'
)

try:
    from app.local_settings import db_config

    DYNAMODB_CONFIG = dict(
        env=db_config['env'],
        region=db_config['region'],
        default_read_capacity=db_config['read_capacity'],
        default_write_capacity=db_config['write_config']
    )
except ImportError as ex:
    # You can add logic here
    raise
except KeyError as ex:
    # You can add logic here
    raise
except Exception as ex:
    # You can add logic here
    pass
