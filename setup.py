import os
from setuptools import setup, find_packages
here = os.path.abspath(os.path.dirname(__file__))

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


VERSION = '0.1.1'  # also update __init__.py
AUTHOR_NAME = 'Adam Erispaha'
AUTHOR_EMAIL = 'aerispaha@gmail.com'

install_requires = [
    'geopandas',
    'shapely',
    'pandas',
    'networkx>=2',
    'numpy',
    'geojson',
    'pyproj',
    ]

setup(name='sewergraph',
      version=VERSION,
      description='Tools for graph calculations on sewer networks',
      author=AUTHOR_NAME,
      url='https://github.com/aerispaha/trace',
      author_email=AUTHOR_EMAIL,
      packages=find_packages(exclude=('tests')),
      install_requires=install_requires,
      long_description=read('README.rst'),
      platforms="OS Independent",
      license="MIT License",
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent",
          "Programming Language :: Python :: 2.7",
      ]
)
