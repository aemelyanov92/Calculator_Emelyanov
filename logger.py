import logging.config

LOGGING_CONFIG = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": { },
    "handlers": { },
    "loggers": { },
    "root": { },
}

logging.config.dictConfig(LOGGING_CONFIG)
