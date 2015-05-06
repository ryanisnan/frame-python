import os
from setuptools import setup, find_packages

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='frame-python',
    version='0.1',
    packages=find_packages(),
    install_requires = ['requests>=2.5.1'],
    include_package_data=True,
    license='MIT License',  # example license
    description='A helper library to simplify the process of storing and retrieving images from the Frame image server within Python projects.',
    long_description=README,
    url='',
    author='Jean-Marc Skopek',
    author_email='jeanmarc@skopek.ca',
    classifiers=[
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        # Replace these appropriately if you are stuck on Python 2.
    ],
)
