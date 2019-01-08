from pkg_resources import get_distribution

from gulliver import __version__


def test_installed_version_should_match_package_version():
    assert get_distribution("gulliver").version == __version__
