# PyPi imports
import pytest

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
    def fake_sendmail(*args):
        pass
    monkeypatch.setattr("smtplib.SMTP.sendmail", fake_sendmail)
    response = client.post("/send-message", data=data)


# Ideally would like to provide the raises parameter
@pytest.mark.xfail()
def test_dated_url_for(app):
    with app.app_context():
        contact.dated_url_for('static', filename=None)
