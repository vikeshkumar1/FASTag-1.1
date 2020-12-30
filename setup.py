try:
	from setuptools import setup
except ImportError:
	from distutils.core import setup
config = {
	'description': 'FasTag is a new way of payment at toll booths which uses Radio Frequency Identification (RFID) technology for making direct payments at toll booths from prepaid/savings account linked to
the FasTag system. This software brings the concept of extending the use of FasTag to challan collection by police and petrol pump payments',
	'author': 'Ruchit Karnawat',
	'url': 'URL to get it at.',
	'download_url': 'https://drive.google.com/open?id=1Ry2pRuXhcD6qM3VRDkoKosueYZewqPmL ',
	'author_email': 'ruchitkarnawat1999@gmail.com',
	'version': '1.0',
	'install_requires': ['nose'],
	'packages': ['FASTAG'],
	'scripts': ['./bin/Run.py'],
	'name': 'FASTAG'
}

setup(**config)