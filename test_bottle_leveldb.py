from bottle import Bottle
from .bottle_leveldb import Plugin

fake_leveldb = 'Pretend this is a LevelDB.'

def test_bottle_leveldb():
    app = Bottle()
    ldb = Plugin(db = fake_leveldb, keyword = 'leveldb')
    app.install(ldb)

    @app.route('/abc')
    def abc(leveldb):
        assert leveldb == fake_leveldb
