import os

PRICELIST_API_REGION = os.environ.get('PRICELIST_API_REGION', 'us-east-1')
UPLOAD_S3_BUCKET = os.environ.get('UPLOAD_S3_BUCKET')
UPLOAD_S3_PREFIX = os.environ.get('UPLOAD_S3_PREFIX')
UPLOAD_S3_CURRENT = os.environ.get('UPLOAD_S3_CURRENT ')

LOG_LEVEL = os.environ.get('LOG_LEVEL', 'INFO')
LOGGING_CONFIG = {
    'version': 1,
    'formatters': {
        'default': {
            'format': '%(asctime)s:%(levelname)s:%(message)s',
        },
    },
    'handlers': {
        'defaultHandler': {
            'class': 'logging.StreamHandler',
            'formatter': 'default',
        },
    },
    'root': {
        'handlers': [
            'defaultHandler',
        ],
        'level': LOG_LEVEL,
    },
}
