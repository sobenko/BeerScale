from setuptools import setup
from setuptools.command.test import test as TestCommand

class PyTest(TestCommand):
    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = ['tests']
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import sys
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

setup(
    name='BeerScale',
    author='Steve Sobenko / Dan Harris',
    version="0.0.1",
    url='http://github.com/sobenko/beerscale',
    packages=['beerscale'],
    description='A server to monitor the weight of beer kegs',
    scripts = ["bin/beerscale"],
    install_requires=['click==3.3', 'pyserial==2.7', 'flask==0.10.1'],
    tests_require=['pytest==2.6.4'],
    cmdclass={'test': PyTest}
)
