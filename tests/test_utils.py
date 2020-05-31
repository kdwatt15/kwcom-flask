# PyPi imports
from os import environ

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
