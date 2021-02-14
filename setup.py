from distutils.core import setup
from setuptools import find_packages
import os

# User-friendly description from README.md
current_directory = os.path.dirname(os.path.abspath(__file__))
try:
    with open(os.path.join(current_directory, 'README.md'), encoding='utf-8') as f:
        long_description = f.read()
except Exception:
    long_description = ''

setup(
	name='stockopedia-scraper',
	packages=find_packages(exclude=['venv']),
	version='1.0.0',
	license='MIT',
	description='Scrap data from Stockopedia website',
	long_description=long_description,
	long_description_content_type='text/markdown',
	author='oluiscabral',
	author_email='oluiscabral@hotmail.com',
	url='https://github.com/oluiscabral/stockopedia-scraper',
	keywords=['scrap', 'scraper', 'stockopedia'],
	install_requires=['beautifulsoup4','cachetools', 'certifi', 'chardet', 'google-auth', 'google-auth-oauthlib', 'gspread', 'idna', 'oauthlib', 'pyasn1', 'pyasn1-modules', 'pytz', 'requests', 'requests-oauthlib', 'rsa', 'selenium', 'six', 'soupsieve', 'urllib3']
)
