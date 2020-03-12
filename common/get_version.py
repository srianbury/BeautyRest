import os


def get_version():
    VERSION = os.getenv('VERSION')
    VERSION_NUMBER = os.getenv('VERSION_NUMBER')
    return '{v}{n}'.format(v=VERSION, n=VERSION_NUMBER)
