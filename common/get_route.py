from .get_version import get_version

def get_route(paths):
    version = get_version()
    rest = '/'.join(paths)
    return '/{v}/{rest}'.format(v=version, rest=rest)