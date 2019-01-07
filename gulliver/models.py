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


"""Data models of the application."""


from newt.db import BTree
from pyramid_zodbconn import get_connection


class Root(BTree):
    """Root of the application."""


def get_root(request):
    """Get the root object of the application.

    :sig: (pyramid.request.Request) -> Root
    :param request: Request to respond to.
    :return: Application root.
    """
    connection = get_connection(request)
    zodb_root = connection.root()
    if "app_root" not in zodb_root:
        zodb_root["app_root"] = Root()
    return zodb_root["app_root"]
