from flask import request
from flask_restful import Resource
from selenium import webdriver
from bs4 import BeautifulSoup
import os


class Main(Resource):
    def post(self):
        json_data = request.get_json(force=True)
        url = json_data['url']
        soup = self._get_soup(url)

        return self._return_json_soup(soup)
    

    def get(self):
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