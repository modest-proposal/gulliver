"""Initialization of the app."""

__version__ = "0.1.0"

from pyramid.config import Configurator


def create_app(global_config, **settings):
    """Create a Gulliver app.

    :param global_config: Global configuration settings.
    :param settings: Extra settings to pass to the configurator.
    :return: Created application.
    """
    config = Configurator(settings=settings)
    config.include("pyramid_chameleon")
    config.scan(".views")
    return config.make_wsgi_app()
