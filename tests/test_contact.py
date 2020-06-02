# PyPi imports
import pytest
from flask import url_for

# Project imports
from kwcom import contact


def test_contact(client):
    client.get("/contact").status_code = 200
    
    
# need better assert statement for this. Might want to seperate the post
# into two paths to allow for better testing
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
    

# need better assert statements for the nex two texts
def test_send_email(app, monkeypatch):
    def placeholder(*args, **kargs):
        return True
    monkeypatch.setattr("smtplib.SMTP.login", placeholder)
    monkeypatch.setattr("smtplib.SMTP.sendmail", placeholder)
    with app.app_context():
        assert contact.send_email() is not None
        
        
def test_send_text(app):
	with app.app_context():
		response = contact.send_text(sender=15005550006)
		assert response.status_code == 302, response.status_code
