import threading, time

import requests
from bottle import Bottle

from bottle_leveldb import Plugin

def test_pass_through():
    fake_leveldb = 'Pretend this is a LevelDB.'

    app = Bottle()
    ldb = Plugin(fake_leveldb, keyword = 'leveldb')
    app.install(ldb)

    @app.route('/')
    def index(leveldb):
        assert leveldb == fake_leveldb
        return fake_leveldb

    t = threading.Thread(None, target = app.run, daemon = True)
    t.start()
    time.sleep(1)
    r = requests.get('http://127.0.0.1:8080/')
    assert r.ok
    assert r.text == fake_leveldb
