# kevin-watt.com
![Build health](https://travis-ci.com/kdwatt15/kwcom.svg?branch=master) [![Coverage Status](https://coveralls.io/repos/github/kdwatt15/kwcom/badge.svg?branch=master)](https://coveralls.io/github/kdwatt15/kwcom?branch=master)

Personal website to be hosted at kevin-watt.com
## Directory Contents
### ~/
* kwcom.wsgi
* requirements.txt
* setup.cfg
* setup.py

### ~/tests
* conftest.py
* test_contact.py
* test_factory.py
* test_mainpages.py
* test_utils.py

### ~/lib/kwcom
* \_\_init\_\_.py
* contact.py
* mainpages.py
* utils.py

#### ./static/
The static directory contains CSS and Javascript files, images, and documents that are served by the website. All CSS is incorporated in the style.css file. Javascript is in the process of being extracted from the HTML and into the script.js file.

#### ./templates/
HTML files to be served by the webpage are stored here. The two directories *mainpages* and *contact* align with the blueprints registed with the Flask app. All of the HTML files extend the base.html file.
