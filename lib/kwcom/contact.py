# Obviously need to clean all of this up
# Standard imports
from os import listdir, stat, environ
from os.path import join
import smtplib

# PyPi imports
from flask import Blueprint
from flask import render_template
from flask import url_for
from flask import redirect
from flask import request
from twilio.rest import Client

# Project specific imports
from kwcom.utils import nav_links
from flask import current_app


contact_bp = Blueprint("contact_bp", __name__)

# need to migrate this to utils and then have in initialization of the app
@contact_bp.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)


def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = join(contact_bp.root_path,
                endpoint, filename)
            values['q'] = int(stat(file_path).st_mtime)
    return url_for(endpoint, **values)

# should I have a decorate to recover errors to one page here?
def send_text(message='test', sender='+12039901186'):
    account_sid = environ['TWILIO_ACCOUNT_SID']
    auth_token = environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=message,
        from_=sender,
        to='+12035367360'
    )
    return redirect(url_for('main_pages.about_me'))
    

def send_email(message=None, recepient='kdwatt15@gmail.com'):
    gmail_user = environ['GMAIL_USER']
    gmail_password = environ['GMAIL_PASSWORD']
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login(gmail_user, gmail_password)
    server.sendmail(gmail_user, recepient, message)
    server.close()
    
    return redirect(url_for('main_pages.about_me'))


@contact_bp.route("/contact")
def contact():
    return render_template(join("mainpages", "contact.html"), 
        nav_links=nav_links())
        
        
@contact_bp.route("/send-message", methods=['POST'])
def send_message():
    message = request.form['body']
    name = "{0} {1}".format(
        request.form['firstName'], request.form['lastName']
    )
    number = request.form['phoneNumber']
    current_app.logger.info(str(len(number)))
    if len(number) == 10:
        message = "\n{0}, {1}:\n\n{2}".format(name, number, message)
        return send_text(message=message)
    else:
        email = request.form['email']
        return send_email(message=message)
