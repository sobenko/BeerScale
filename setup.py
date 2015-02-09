from setuptools import setup

setup(
    name='BeerScale',
    author='Steve Sobenko / Dan Harris',
    version="0.0.1",
    url='http://github.com/sobenko/beerscale',
    packages=['beerscale'],
    description='A server to monitor the weight of beer kegs',
    scripts = ["bin/beerscale"]
)
