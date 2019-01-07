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


"""Handlers for the HTTP requests to the endpoints of the application."""

from pyramid.view import view_config

from .models import Root


# sigalias: Request = pyramid.request.Request


@view_config(context=Root, renderer="templates/home.pt")
def view_root(request):
    """Respond to a request to the root.

    :sig: (Request) -> Dict
    :param request: Incoming HTTP request.
    :return: Page data.
    """
    page_title = "Gulliver"
    return {"page_title": page_title}
