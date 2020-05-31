# PyPi imports
import pytest
from dotenv import load_dotenv

# Project imports
import kwcom


@pytest.fixture
def app():
    load_dotenv()
    test_config = {
        "TESTING": True,
        # Server name has to be set to allow URLs to be generated
        # without making requests
        "SERVER_NAME": "127.0.0.1 localhost.dev"
    }
    return kwcom.create_app(test_config=test_config)


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()
