# our configuration file which configures our flask app aka tells it all
# the specific details it needs to know about this psecific app via variables

from datetime import timedelta
import os #operatin system, necessary for python application so python can be intepreted on any os
from dotenv import load_dotenv #allows us to load our enviroment variables from a different file(so we can secure them)


# establish our base directory so when we use "." in app it knows that ranger_shop is our base dir
basedir = os.path.abspath(os.path.dirname(__file__))

#establish where our envirment variables are coming from 
load_dotenv(os.path.join(basedir, '.env'))



#create our config class
class Config():
    """
    create config class which will setup our configuration variables
    using environment variable where available otherwise create config variables
    """


    FLASK_APP = os.environ.get('FLASK_APP')#looking fo rkey of FLASK_APP in .env file
    FLASK_ENV = os.environ.get('FLASK_ENV')
    FLASK_DEBUG = os.environ.get('FLASK_DEBUG')
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'literally can be whatever you want'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False # we dont want amessage every singe time our database changes
    JWT_SECRET_KEY = os.environ.get('JWT_SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(days=365)