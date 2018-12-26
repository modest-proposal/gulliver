import webtest
from pytest import fixture

from gulliver import create_app


@fixture(scope="module")
def app():
    app_ = create_app({})
    return webtest.TestApp(app_)


def test_get_home(app):
    response = app.get("/", status=200)
    assert b"<h1>Gulliver" in response.body
