from os import getenv

from src import create_app


environment = getenv('FLASK_ENV')
application = create_app(environment)

if __name__ == '__main__':
    application.run('0.0.0.0')
