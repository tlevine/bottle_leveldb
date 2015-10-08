import inspect

class Plugin(object):
    name = 'leveldb'
    api = 2

    def setup(self, app):
        pass

    def apply(self, callback, route):
        return
        args = inspect.getargspec(context['callback'])[0]
        if keyword not in args:
            return callback

    def close(self):
        pass
