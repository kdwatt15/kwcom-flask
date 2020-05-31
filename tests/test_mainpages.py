#PyPi imports
import pytest

# Project imports
from kwcom import mainpages


def test_about_me(client):
    assert client.get("/").status_code == 200
    

def test_skills(client):
    assert client.get("/skills").status_code == 200


def test_experience(client):
    assert client.get("/experience").status_code == 200
    
    
def test_projects(client):
    assert client.get("/projects").status_code == 200
    

# Ideally would like to provide the raises parameter
@pytest.mark.xfail()
def test_dated_url_for(app):
    with app.app_context():
        mainpages.dated_url_for('static', filename=None)
