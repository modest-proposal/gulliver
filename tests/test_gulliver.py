from pyramid.testing import DummyRequest

from gulliver import __version__, views


def test_version():
    assert __version__ == "0.1.0"


def test_get_home_should_contain_page_title():
    request = DummyRequest()
    response = views.home(request)
    assert response.get("page_title") == "Gulliver"
