from os.path import dirname, join


activate_this = join(dirname(__file__), 'bin', 'activate_this.py')
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

from kwcom import create_app
application = create_app()
