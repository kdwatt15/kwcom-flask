# PyPi imports
import pytest
from flask import url_for

# Project imports
from kwcom import contact


def test_contact(client):
    client.get("/contact").status_code = 200
    
@pytest.mark.parametrize(
    ("firstName", "lastName", "email", "phoneNumber", "body"),
    (
        ("first", "last", "email@test.com", "", "test email body"),
        ("first", "last", "", "5555555555", "test text body")
    )
)
def test_send_message(client, monkeypatch, firstName, lastName, email, 
    phoneNumber, body):
    data = {
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "phoneNumber": phoneNumber,
        "body": body
    }
    def placeholder(*args, **kargs):
        return client.get("/")
    monkeypatch.setattr("kwcom.contact.send_email", placeholder)
    monkeypatch.setattr("kwcom.contact.send_text", placeholder)
    response = client.post("/send-message", data=data)
    

def test_send_email(app, monkeypatch):
    def placeholder(*args, **kargs):
        return True
    monkeypatch.setattr("smtplib.SMTP.login", placeholder)
    monkeypatch.setattr("smtplib.SMTP.sendmail", placeholder)
    with app.app_context():
        assert contact.send_email() is not None
        
        
def test_send_text(app):
    with app.app_context():
        assert contact.send_text() is not None


# Ideally would like to provide the raises parameter
@pytest.mark.xfail()
def test_dated_url_for(app):
    with app.app_context():
        contact.dated_url_for('static', filename=None)
