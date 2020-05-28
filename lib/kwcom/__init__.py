import os
import kwcom

from flask import Flask
from flask import url_for
from flask import redirect


def create_app():
    app = Flask(__name__, instance_relative_config=True)
    
    @app.route('/hello')
    def index_page():
        return 'hello'
        
    from kwcom.mainpages import main_pages
    
    app.register_blueprint(main_pages)
    
    return app
