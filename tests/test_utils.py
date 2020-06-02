# Standard imports
from os import environ

# PyPi imports
import pytest

# Project imports
from kwcom import utils

def set_twilio_env():
    utils.set_twilio_env()
    env_keys = ("TWILIO_ACCOUNT_SID", "TWILIO_AUTH_TOKEN", "GMAIL_USER",
        "GMAIL_PASSWORD")
    for key in env_keys:
        assert environ[key]
        
        
def test_nav_links(app):
    with app.app_context():
        assert utils.nav_links() is not None
     
    
def test_fetch_banner_images():
    assert utils.fetch_banner_images("employers") is not None

# Want to figure out why I still have to xfail this
#@pytest.mark.xfail()
def test_dated_url_for(app):
	# monkeypatch used to prevent url for from returning error
	def placeholder(*args, **kargs):
		return client.get("/")
	with app.app_context():
		try:
			utils.dated_url_for('static', filename=None)
		except Exception as e:
			assert "Could not build url for endpoint 'static'" in str(e)
