BLUEPRINTS = [
    'app.review',
]

try:
    from app.local_settings import db_config

    DYNAMODB_CONFIG = dict(
        env=db_config['env'],
        region=db_config['region'],
        default_read_capacity=db_config['read_capacity'],
        default_write_capacity=db_config['write_config']
    )
except Exception:
    pass
