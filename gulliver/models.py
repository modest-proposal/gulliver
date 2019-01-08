# Copyright (C) 2019 H. Turgut Uyar <uyar@tekir.org>
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


"""Data models of the application."""


from persistent.mapping import PersistentMapping
from pyramid_zodbconn import get_connection


class Root(PersistentMapping):
    """Root of the application."""

    __parent__ = None
    __name__ = None


def get_root(request):
    """Get the root of the application's data model.

    :sig: (pyramid.request.Request) -> Root
    :param db_root: Root of the database connection.
    :return: Root model.
    """
    connection = get_connection(request)
    db_root = connection.root()
    app_root = db_root.get("gulliver")
    if app_root is None:
        app_root = Root()
        db_root["gulliver"] = app_root
    return app_root
