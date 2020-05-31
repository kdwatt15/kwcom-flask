# Standard imports
import os

# PyPi imports
from flask import Flask
from flask import url_for
from flask import redirect


def create_app():
    app = Flask(__name__, instance_relative_config=True)
        
    from kwcom.utils import set_twilio_env
    set_twilio_env()
        
    from kwcom.mainpages import main_pages
    app.register_blueprint(main_pages)
    
    from kwcom.contact import contact_bp
    app.register_blueprint(contact_bp)
    
    return app
