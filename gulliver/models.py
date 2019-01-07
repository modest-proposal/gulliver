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


class Root(BTree):
    """Root of the application."""


def get_app_root(db_root):
    """Get the root of the application's data model.

    :sig: (persistent.mapping.PersistentMapping) -> Root
    :param db_root: Root of the database connection.
    :return: Root model.
    """
    app_root = db_root.get("app_root")
    if app_root is None:
        app_root = Root()
        db_root["app_root"] = app_root
    return app_root
