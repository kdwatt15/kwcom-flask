# Standard imports
import os

# PyPi imports
from flask import Flask
from flask import url_for
from flask import redirect

# Project imports
from kwcom.utils import dated_url_for


def create_app(test_config=None):
	app = Flask(__name__, instance_relative_config=True)
	# This is kept in for best practice. Need to understand the use of
	# a secret key in the future and incorporate it.
	app.config.from_mapping()

	if test_config is not None:
		app.config.update(test_config)
	else:
		from kwcom.utils import set_twilio_env
		set_twilio_env()
		
	from kwcom.mainpages import main_pages
	app.register_blueprint(main_pages)

	from kwcom.contact import contact_bp
	app.register_blueprint(contact_bp)

	@app.context_processor
	def override_url_for():
		return dict(url_for=dated_url_for)

	return app
