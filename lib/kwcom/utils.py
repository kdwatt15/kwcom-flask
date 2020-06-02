#Standard imports
from os import listdir, stat
from os.path import join, dirname
from pathlib import Path

#PyPi imports
from flask import url_for
from flask import current_app
from imghdr import what
from dotenv import load_dotenv


def set_twilio_env():
    """Set environment variables to support the use of twilio."""
    load_dotenv(join(dirname(__file__), '.env'))
    
    
def nav_links():
    page_names = ["skills", "experience", "projects"]
    # if (name is not None): page_names.remove(name)
    links = [url_for("main_pages.{0}".format(name)) for name in page_names]
    return links
    
    
def fetch_banner_images(folder_name):
    comp_path = join(dirname(__file__), "static", "images", folder_name)
    img_types = ('.svg', '.png', '.jpg')
    comp_images = [f for f in listdir(comp_path) if Path(f).suffix in img_types]
    return comp_images


def dated_url_for(endpoint, **values):
	with current_app.app_context():
		if endpoint == 'static':
			filename = values.get('filename', None)
			if filename:
				file_path = join(current_app.root_path,
					endpoint, filename)
				values['q'] = int(stat(file_path).st_mtime)
	return url_for(endpoint, **values)
