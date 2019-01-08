from gulliver.models import __version__, Root


def test_version_of_new_model_should_be_latest():
    root = Root()
    assert root.metadata.version == __version__
