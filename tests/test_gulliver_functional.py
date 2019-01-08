import webtest
from pytest import fixture

from configparser import ConfigParser
from http.server import HTTPStatus
from pathlib import Path

from gulliver import create_app


_CONFIG_FILE = Path(__file__).parent / "testing.ini"


@fixture(scope="module")
def app():
    """A Gulliver application instance for testing."""
    parser = ConfigParser()
    parser.read(_CONFIG_FILE)
    settings = parser["app:main"]
    app_ = create_app({}, **settings)
    return webtest.TestApp(app_)


def test_get_root_should_contain_page_title_in_heading(app):
    response = app.get("/", status=HTTPStatus.OK)
    assert b"<h1>Gulliver" in response.body
