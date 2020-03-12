from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from dotenv import load_dotenv
from resources.Main.resource import Main
from common.get_version import get_version
from common.get_route import get_route


# setup / vars
load_dotenv()
app = Flask(__name__)
CORS(app)
api = Api(app)


# add resources
api.add_resource(Main, get_route(['soup']))


if __name__ == '__main__':
    app.run(debug=True)
