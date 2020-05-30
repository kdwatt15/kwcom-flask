import os

from flask import Flask
from flask import url_for
from flask import redirect


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    @app.route('/hello')
    def index_page():
        return 'hello'
        
    from kwcom import mainpages
    app.register_blueprint(mainpages.main_pages)
    
    from kwcom import contact
    app.register_blueprint(contact.contact_bp)
    contact.init_contact(app)
    
    return app
