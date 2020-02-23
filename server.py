from flask import Flask
from flask_restful import Resource, Api


app = Flask(__name__)
api = Api(app)


VERSION = 'v1'


class Main(Resource):
    def get(self):
        return { 'hello': 'world' }


api.add_resource(Main, '/{VERSION}/soup'.format(VERSION=VERSION))


if __name__ == '__main__':
    app.run(debug=True)

