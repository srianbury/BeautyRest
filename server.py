from flask import Flask
from flask_restful import Api
from flask_cors import CORS
import os
from dotenv import load_dotenv
from resources.Main.resource import Main


# setup / vars
load_dotenv()
app = Flask(__name__)
CORS(app)
api = Api(app)
VERSION = os.getenv('VERSION')
VERSION_NUMBER = os.getenv('VERSION_NUMBER')


# add resources
api.add_resource(Main, '/{VERSION}{VERSION_NUMBER}/soup'.format(VERSION=VERSION, VERSION_NUMBER=VERSION_NUMBER))


if __name__ == '__main__':
    app.run(debug=True)

