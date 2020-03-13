from flask import request
from flask_restful import Resource, reqparse
from selenium import webdriver
from bs4 import BeautifulSoup
import os
from common import constants
from common.get_route import get_route


class Main(Resource):
    def __init__(self):
        self.route = get_route(['soup'])


    def post(self):
        json_data = request.get_json(force=True)
        url = json_data['url']
        soup = self._get_soup(url)

        return self._return_json_soup(soup)
    

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('url', required=True, help=constants.ERROR_PARAM_URL)
        args = parser.parse_args()

        url = self._get_url(request.args)
        soup = self._get_soup(url)
        return self._return_json_soup(soup)
    

    def _return_json_soup(self, soup):
        return { 'soup' : str(soup) }
    

    def _get_soup(self, url):
        soup = None
        with self._get_driver() as driver:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
        return soup
    

    # get url from args
    def _get_url(self, args):
        BASE_URL_PARAM = 'url'
        url = args[BASE_URL_PARAM]
        for key in args:
            if(key != BASE_URL_PARAM):
                url += '&{key}={val}'.format(key=key, val=args[key])
        return url
    

    def _get_driver(self):
        options = webdriver.ChromeOptions()
        options.binary_location = os.getenv('GOOGLE_CHROME_BIN')
        options.add_argument('--headless')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('--no-sandbox')
        driver = webdriver.Chrome(executable_path=os.getenv('CHROMEDRIVER_PATH'), chrome_options=options)
        return driver