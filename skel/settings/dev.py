"""Development settings and globals."""


from .common import CommonConfig


class DevConfig(CommonConfig):

    # Debug settings:
    DEBUG = True
    TESTING = DEBUG
