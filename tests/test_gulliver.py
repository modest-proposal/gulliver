from pyramid.testing import DummyRequest

from pkg_resources import get_distribution

from gulliver import __version__, views


def test_version():
    assert get_distribution("gulliver").version == __version__


def test_get_home_should_contain_page_title():
    request = DummyRequest()
    response = views.home(request)
    assert response.get("page_title") == "Gulliver"
