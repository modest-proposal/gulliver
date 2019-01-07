# Copyright (C) 2018-2019 H. Turgut Uyar <uyar@tekir.org>
#
# Gulliver is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Gulliver is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Gulliver.  If not, see <http://www.gnu.org/licenses/>.


"""Initialization of the application."""


__version__ = "0.1.0"  # sig: str


from pyramid.config import Configurator

from .models import get_root


def create_app(global_config, **settings):
    """Create a Gulliver app.

    :sig: (Mapping) -> pyramid.router.Router
    :param global_config: Global configuration settings.
    :param settings: Extra settings to pass to the configurator.
    :return: Created application.
    """
    with Configurator(settings=settings) as config:
        config.include("pyramid_chameleon")
        config.set_root_factory(get_root)
        config.scan(".views")
        return config.make_wsgi_app()
