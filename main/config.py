import os

# uncomment the line below for postgres database url from environment variable
CITYDB_CONNECTION_SERVER = os.getenv('CITYDB_CONNECTION_SERVER', '3dcitydb')
#print(os.getenv('CITYDB_CONNECTION_SERVER', '3dcitydb'))
CITYDB_CONNECTION_PORT = os.getenv('CITYDB_CONNECTION_PORT', '5432')
CITYDB_CONNECTION_SID = os.getenv('CITYDB_CONNECTION_SID', '4d_participatory_app')
CITYDB_CONNECTION_USER = os.getenv('CITYDB_CONNECTION_USER', 'postgres')
CITYDB_CONNECTION_PASSWORD = os.getenv('CITYDB_CONNECTION_PASSWORD', 'postgres')

POSTGRES_USER=CITYDB_CONNECTION_USER
POSTGRES_PW=CITYDB_CONNECTION_PASSWORD
POSTGRES_URL='{server}:{port}'.format(server=CITYDB_CONNECTION_SERVER,port=CITYDB_CONNECTION_PORT)
POSTGRES_DB_DEV="4d_participatory_app_dev"
POSTGRES_DB_CITY="citydb"
POSTGRES_DB_PROD="4d_participatory_app_prod"
POSTGRES_DB_TEST="4d_participatory_app_test"

DB_URL_DEV = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB_DEV)
DB_URL_PROD = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB_PROD)
DB_URL_TEST = 'postgresql://{user}:{pw}@{url}/{db}'.format(user=POSTGRES_USER,pw=POSTGRES_PW,url=POSTGRES_URL,db=POSTGRES_DB_TEST)

#basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', 'my_pr3cious_secret_key')
    DEBUG = False


class DevelopmentConfig(Config):
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = DB_URL_DEV
    DEBUG = True
    #SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_main.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class TestingConfig(Config):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = DB_URL_TEST #'sqlite:///' + os.path.join(basedir, 'flask_boilerplate_test.db')
    PRESERVE_CONTEXT_ON_EXCEPTION = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class ProductionConfig(Config):
    DEBUG = False
    # uncomment the line below to use postgres
    SQLALCHEMY_DATABASE_URI = DB_URL_PROD


config_by_name = dict(
    dev=DevelopmentConfig,
    test=TestingConfig,
    prod=ProductionConfig
)

key = Config.SECRET_KEY