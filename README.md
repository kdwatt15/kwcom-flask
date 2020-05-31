# kevin-watt.com
![Build health](https://travis-ci.com/kdwatt15/kwcom.svg?branch=master) ![Coverage Status](https://coveralls.io/repos/github/kdwatt15/kwcom/badge.svg?branch=master)

Personal website hosted at http://kevin-watt.com. Website is hosted on an Ubuntu 14.04 server using [mod_wsgi](https://modwsgi.readthedocs.io/en/develop/).
## Directory Contents
### ~/
* .travis.yml
  * Configuration for integration with [Travis CI](https://travis-ci.org/) and [Coveralls](https://coveralls.io/) for build and coverage tracking
* kwcom.wsgi
  * WSGI file for use by the mod_wsgi-express function
* requirements.txt
  * Exhaustive in the scope of development. Modules included for production are listed below.
* setup.cfg
  * Configuration for the __setup.py__ file.
* setup.py
  * Configuration is inherited from __setup.cfg__. Requirements are populated by reading the __requirements.txt__ file.

### ~/tests
* conftest.py
  * Establishes the context for the tests listed below. More details on testing in the testing section
* test_contact.py
  * Tests the __contact.py__ file
* test_factory.py
  * Tests the __\_\_init\_\_.py__ file
* test_mainpages.py
  * Tests the __mainpages.py__ file
* test_utils.py
  * Tests the __utils.py__ file.

### ~/lib/kwcom
* \_\_init\_\_.py
  * kwcom uses an [application factory](https://flask.palletsprojects.com/en/1.1.x/patterns/appfactories/) structure. The _create\_app_ function creates the Flask application. It takes a testing configuration as an input. If the testing configuration is not present, the _dotenv.load\_dotenv_ function will be called to safely set environment variables to be accessed by the application
* contact.py
  * The [contact](http://kevin-watt.com/contact) works through the _contact\_bp_ blueprint. This uses the [smtplib](https://docs.python.org/3/library/smtplib.html) to send emails and [Twilio](https://www.twilio.com/docs/libraries/python) to send text messages
* mainpages.py
  * The _main\_pages_ blueprint is configures the routes for the [home](http://kevin-watt.com), [skills](http://kevin-watt.com/skills), [experience](http://kevin-watt.com/experience), and [projects](http://kevin-watt.com/projects) pages
* utils.py
  * the _utils_ file contains functions that are used across the multiple modules.

#### ./static
The static directory contains CSS and Javascript files, images, and documents that are served by the website. All CSS is incorporated in the style.css file. Javascript is in the process of being extracted from the HTML and into the script.js file.

#### ./templates
HTML files to be served by the webpage are stored here. The two directories *mainpages* and *contact* align with the blueprints registed with the Flask app. All of the HTML files extend the base.html file.
