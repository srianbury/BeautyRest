from flask import Flask, request
from flask_restful import Resource, Api
from selenium import webdriver
from bs4 import BeautifulSoup
from flask_cors import CORS
import os


app = Flask(__name__)
CORS(app)
api = Api(app)


VERSION = 'v1'


class Main(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        url = json_data['url']

        options = webdriver.ChromeOptions()
        options.binary_location = os.environ.get('GOOGLE_CHROME_BIN')
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')

        driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), chrome_options=options)
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        driver.close()

        return { 'soup': str(soup) }


api.add_resource(Main, '/{VERSION}/soup'.format(VERSION=VERSION))


if __name__ == '__main__':
    app.run(debug=True)

