# Project imports
from kwcom import create_app

def test_config():
    """Test create_app without passing test config."""
    # This is taken from the flask tutorial.
    # No need to overcomplicate things
    assert not create_app().testing
    assert create_app({"TESTING": True}).testing
