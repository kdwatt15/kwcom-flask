from os import stat
from os.path import join

from pathlib import PureWindowsPath

from flask import Blueprint
from flask import render_template
from flask import url_for

from kwcom.utils import nav_links, fetch_banner_images


main_pages = Blueprint("main_pages", __name__)


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
