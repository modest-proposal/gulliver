import webtest
from pytest import fixture

import os
from configparser import ConfigParser
from http.server import HTTPStatus

from gulliver import create_app


_CONFIG_FILE = os.path.join(os.path.dirname(__file__), "testing.ini")


@fixture(scope="module")
def app():
    """A Gulliver application instance for testing."""
    parser = ConfigParser()
    parser.read(_CONFIG_FILE)
    settings = parser["app:main"]
    app_ = create_app({}, **settings)
    return webtest.TestApp(app_)


def test_get_home_should_contain_page_title_as_heading(app):
    response = app.get("/", status=HTTPStatus.OK)
    assert b"<h1>Gulliver" in response.body
