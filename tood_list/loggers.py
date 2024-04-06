import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LOG_FORMAT = '[%(asctime)s]-[%(levelname)s]-[%(pathname)s]-[Func:%(funcName)s]-[Line:%(lineno)s]-[%(message)s]'

path = os.path.join(BASE_DIR, 'logs/')
logger_path_existed = os.path.exists(path)
if not logger_path_existed:
    os.mkdir(path)


LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
    'formatters': {
        'verbose': {
            'format': LOG_FORMAT
        },
        'simple': {
            'format': LOG_FORMAT
        },
    },
    'handlers': {
        'disaster': {
            'level': 'ERROR',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'interval': 1,
            'when': 'midnight',
            'backupCount': 3,
            'filename': os.path.join(BASE_DIR, 'logs', 'disaster.log'),
            'formatter': 'simple'
        },
        'process_handler': {
            'level': 'INFO',
            'class': 'logging.handlers.TimedRotatingFileHandler',
            'interval': 1,
            'when': 'midnight',
            'backupCount': 3,
            'filename': os.path.join(BASE_DIR, 'logs', 'main_process.log'),
            'formatter': 'simple'
        },

    },
    'loggers': {
        'main': {
            'handlers': ['process_handler'],
            'level': 'INFO',
            'propagate': False,
        },
        'disaster': {
            'handlers': ['disaster'],
            'level': 'ERROR',
            'propagate': False,
        },
    }
}
