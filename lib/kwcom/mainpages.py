from os import stat, fspath
from os.path import join

from pathlib import PureWindowsPath

from flask import Blueprint
from flask import render_template
from flask import url_for

from kwcom.utils import nav_links, fetch_banner_images


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
    

@main_pages.route("/")
def about_me():
    return render_template('mainpages/about-me.html', 
        nav_links=nav_links(), 
        comp_images=fetch_banner_images("employers"),
        background_img = "blue-light.jpg")


@main_pages.route("/experience")
def experience():
    return render_template("mainpages/experience.html", 
        nav_links=nav_links(), 
        background_img = "black-highway-road.png")


@main_pages.route("/skills")
def skills():
    return render_template("mainpages/skills.html", 
        nav_links=nav_links(),
        background_img = "computer-background.jpg")
    
    
@main_pages.route("/projects")
def projects():
    return render_template("mainpages/projects.html", 
        nav_links=nav_links(),
        background_img = "garage.jpg")
