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

