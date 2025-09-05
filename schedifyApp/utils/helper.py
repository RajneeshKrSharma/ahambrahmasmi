from schedifyApp.models import Config


def get_config_value(key: str, default=None):
    try:
        config = Config.objects.get(key=key)
        return config.value
    except Config.DoesNotExist:
        return default