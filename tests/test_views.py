from pyramid.testing import DummyRequest

from gulliver import views


def test_view_root_should_report_application_name_as_page_title():
    request = DummyRequest()
    response = views.view_root(request)
    assert response.get("page_title") == "Gulliver"
