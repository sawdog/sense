import confuse


config = confuse.LazyConfig('pySense', __name__)
CONFIG_DIR = config.config_dir()
USER_CONFIG_PATH = config.user_config_path()
template = {
    'package': str,
    'handlers': {
        'date': {
            'arrow_format': str,
            'default_format': str,
            'query_format': str,
        },
        'datetime': {
            'arrow_format': str,
            'default_format': str,
        },
    },
    'environment': str,
    'logging': {
        'name': str,
        'level': str,
        'propigate': bool,
    },
    'sense': {
        'username': str,
        'password': str,
        'api': {
            'url': str,
            'timeout': int,
        },
        'realtime': {
            'url': str,
        },
    },
    'sentry': {
        'enable': bool,
        'dsn': str
    },
    'websocket': {
        'timeout': int,
    }
}
yamlcfg = config.get(template)
