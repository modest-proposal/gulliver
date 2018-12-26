__version__ = "0.1.0"

from pyramid.config import Configurator


def create_app(global_config, **settings):
    config = Configurator(settings=settings)
    config.include("pyramid_chameleon")
    config.scan(".views")
    return config.make_wsgi_app()
