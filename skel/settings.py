"""App settings and globals."""


class BaseConfig(object):
    """Base settings and globals."""

    # Debug settings:
    DEBUG = False
    TESTING = DEBUG


class DevConfig(BaseConfig):
    """Development settings and globals."""

    # Debug settings:
    DEBUG = True
    TESTING = DEBUG


class TestConfig(BaseConfig):
    """Development settings and globals."""

    # Debug settings:
    DEBUG = True
    TESTING = DEBUG


class ProdConfig(BaseConfig):
    """Production settings and globals."""
    pass
