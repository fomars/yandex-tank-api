#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# Allow trove classifiers in previous python versions
from sys import version
if version < '2.2.3':
    from distutils.dist import DistributionMetadata
    DistributionMetadata.classifiers = None
    DistributionMetadata.download_url = None

from yandex_tank_api import __version__ as version

def requireModules(moduleNames=None):
    import re
    if moduleNames is None:
        moduleNames = []
    else:
        moduleNames = moduleNames

    commentPattern = re.compile(r'^\w*?#')
    moduleNames.extend(
        filter(lambda line: not commentPattern.match(line),
            open('requirements.txt').readlines()))

    return moduleNames

setup(
    name='yandex-tank-api',
    version=version,

    author='Andrei Sekretenko',
    author_email='asekretenko@gmail.com',

    description='Yandex.Tank HTTP API',
    long_description=open('README.txt').read(),
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers'
    ],

    install_requires=requireModules(),
    packages=['yandex_tank_api'],
    package_dir={'yandex_tank_api': 'yandex_tank_api'},
    package_data={
        'yandex_tank_api': [
            'templates/*.jade',
            'static/css/*.css',
            'static/favicon.ico',
            'static/fonts/*',
            'static/js/*.js',
            'static/js/vendor/ace/*.js',
            'static/js/vendor/*.js',
            'config/*'
        ],
    },
    scripts=['scripts/yandex-tank-api-server'],
    test_suite='yandex-tank-api',
)
