from pyramid.view import view_config


@view_config(name="", renderer="templates/home.pt")
def home(request):
    page_title = "Gulliver"
    return {"page_title": page_title}
