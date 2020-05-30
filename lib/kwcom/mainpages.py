from os import listdir, stat
from os.path import isfile, join, dirname

from pathlib import Path

from imghdr import what

from flask import Blueprint
from flask import render_template
from flask import url_for

main_pages = Blueprint("main_pages", __name__)


@main_pages.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = join(main_pages.root_path,
                endpoint, filename)
            values['q'] = int(stat(file_path).st_mtime)
    return url_for(endpoint, **values)
    
    
def nav_links(name=None):
    page_names = ["skills", "experience", "projects"]
    # if (name is not None): page_names.remove(name)
    links = [url_for("main_pages.{0}".format(name)) for name in page_names]
    return links
    
    
def fetch_banner_images(folder_name):
    comp_path = join(dirname(__file__), "static", "images", folder_name)
    img_types = ('.svg', '.png', '.jpg')
    comp_images = [f for f in listdir(comp_path) if Path(f).suffix in img_types]
    return comp_images
    

@main_pages.route("/")
def about_me():
    return render_template(join("mainpages", "about-me.html"), 
        nav_links=nav_links(), 
        comp_images=fetch_banner_images("employers"),
        background_img = "snowy-mountain-road.jpg")


@main_pages.route("/experience")
def experience():
    return render_template(join("mainpages", "experience.html"), 
        nav_links=nav_links(), 
        background_img = "black-highway-road.png")


@main_pages.route("/skills")
def skills():
    return render_template(join("mainpages", "skills.html"), 
        nav_links=nav_links(),
        background_img = "computer-background.jpg")
    
    
@main_pages.route("/projects")
def projects():
    return render_template(join("mainpages", "projects.html"), 
        nav_links=nav_links(),
        background_img = "sunset-road.jpg")
