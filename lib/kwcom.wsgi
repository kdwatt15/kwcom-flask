activate_this = '/var/www/kwcom/bin/activate'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from kwcom import create_app
application = create_app()
