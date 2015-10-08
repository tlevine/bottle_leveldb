from distutils.core import setup

setup(name='bottle_leveldb',
      author='Thomas Levine',
      author_email='_@thomaslevine.com',
      description='LevelDB plugin for bottle',
      url='http://dada.pink/bottle_leveldb/',
      packages=['bottle_leveldb'],
      tests_require = [
          'pytest>=2.6.4',
      ],
      version='0.0.1',
      license='LGPL',
)
