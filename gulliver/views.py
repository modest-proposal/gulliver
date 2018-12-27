"""Handlers for the HTTP requests to the endpoints of the app."""

from pyramid.view import view_config


# sigalias: Request = pyramid.request.Request


@view_config(name="", renderer="templates/home.pt")
def home(request):
    """Respond to a request to the root.

    :sig: (Request) -> Dict
    :param request: Incoming HTTP request.
    :return: Page data.
    """
    page_title = "Gulliver"
    return {"page_title": page_title}
