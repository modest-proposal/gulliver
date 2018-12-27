import webtest
from pytest import fixture

from http.server import HTTPStatus

from gulliver import create_app


@fixture(scope="module")
def app():
    """A Gulliver application instance for testing."""
    app_ = create_app({})
    return webtest.TestApp(app_)


def test_get_home_should_contain_page_title_as_heading(app):
    response = app.get("/", status=HTTPStatus.OK)
    assert b"<h1>Gulliver" in response.body
