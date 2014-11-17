import os
import ConfigParser

from logging.handlers import RotatingFileHandler

from flask import Flask
from flask.ext.pymongo import PyMongo

from utils.utils import Utils

# Create MongoDB database object.
mongo = PyMongo()
utils = Utils()


def create_app():
    ''' Create the Flask app.
    '''
    # Create the Flask app.
    app = Flask(__name__)

    # Load application configurations
    load_config(app)

    # Configure logging.
    configure_logging(app)

    # Register URL rules.
    register_url_rules(app)

    # Init app for use with this PyMongo
    # http://flask-pymongo.readthedocs.org/en/latest/#flask_pymongo.PyMongo.init_app
    mongo.init_app(app, config_prefix='MONGO')

    return app


def load_config(app):
    ''' Reads the config file and loads configuration properties into the Flask app.
    :param app: The Flask app object.
    '''

    # Get the path to the application directory, that's where the config file resides.
    par_dir = os.path.join(__file__, os.pardir)
    par_dir_abs_path = os.path.abspath(par_dir)
    app_dir = os.path.dirname(par_dir_abs_path)

    # Read config file
    # FIXME: Use the "common pattern" described in "Configuring from Files": http://flask.pocoo.org/docs/config/
    config = ConfigParser.RawConfigParser()
    config_filepath = app_dir + '/config.cfg'
    config.read(config_filepath)

    # Set up config properties
    app.config['SERVER_PORT'] = config.get('Application', 'SERVER_PORT')
    app.config['BASE_PATH'] = config.get('Application', 'BASE_PATH')

    app.config['MONGO_DBNAME'] = config.get('Mongo', 'DB_NAME')

    # Logging path might be relative or starts from the root.
    # If it's relative then be sure to prepend the path with the application's root directory path.
    log_path = config.get('Logging', 'PATH')
    if log_path.startswith('/'):
        app.config['LOG_PATH'] = log_path
    else:
        app.config['LOG_PATH'] = app_dir + '/' + log_path

    app.config['LOG_LEVEL'] = config.get('Logging', 'LEVEL').upper()

    # Set the secret key, keep this really secret. We need this for session manager.
    # Check out sectopm "How to generate good secret keys" in http://flask.pocoo.org/docs/quickstart/
    app.secret_key = config.get('Application', 'SECRET_KEY')


def configure_logging(app):
    ''' Configure the app's logging.
    :param app: The Flask app object.
    '''

    log_path = app.config['LOG_PATH']
    log_level = app.config['LOG_LEVEL']

    # If path directory doesn't exist, create it.
    log_dir = os.path.dirname(log_path)
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    # Create and register the log file handler.
    log_handler = RotatingFileHandler(log_path, maxBytes=250000, backupCount=5)
    log_handler.setLevel(log_level)
    app.logger.addHandler(log_handler)

    # First log informs where we are logging to. Bit silly but serves  as a confirmation that logging works.
    # FIXME: Logging isn't working, figure out why.
    app.logger.info('Logging to: %s', log_path)


# Import forms
from views.index import Index
from views.profile import Profile
from views.resume import Resume
from views.forms.person import Person
from views.forms.search import Search
from views.json.search import SearchRequest


def register_url_rules(app):
    ''' Register the URL rules.
        Use pluggable class-based views: http://flask.pocoo.org/docs/views/
    :param app: The Flask application instance.
    '''

    # Index page.
    app.add_url_rule('/', view_func=Index.as_view('index'))

    # Profile page.
    app.add_url_rule('/profile/<string:id>', view_func=Profile.as_view('profile'))

    # Generate Resume.
    app.add_url_rule('/resume/<string:resume_id>/<int:template_id>', view_func=Resume.as_view('resume'))

    # Registration form.
    app.add_url_rule('/person', view_func=Person.as_view('person'))

    # Registration form.
    app.add_url_rule('/student', view_func=Person.as_view('student'))

    # Search form.
    app.add_url_rule('/search', view_func=Search.as_view('search'))

    # Search request
    app.add_url_rule('/json/search', view_func=SearchRequest.as_view('search_request'))
