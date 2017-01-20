import os.path
from pip.download import PipSession
from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

install_reqs = parse_requirements(os.path.join(os.path.dirname(__file__), 'requirements.txt'), session=PipSession())
reqs = [str(ir.req) for ir in install_reqs]


def read(filename):
    return open(os.path.join(os.path.dirname(__file__), filename)).read()


setup(
    name='nyt-prb-scraper',
    version='0.0.10',
    author='Jeremy Bowers',
    author_email='jeremy.bowers@nytimes.com',
    url='https://github.com/newsdev/nyt-prb-scraper',
    description='A client for scraping and parsing the Periodic Review Secretariat\'s web page for Guananamo detainees.',
    long_description=read('README.rst'),
    packages=('prb',),
    entry_points={
        'console_scripts': (
            'initial_review = prb:initial_review',
            'file_review = prb:file_review',
            'full_review = prb:full_review',
        ),
    },
    license="Apache License 2.0",
    keywords='national security guantanamo bay criminal justice department of defense',
    install_requires=reqs
)
