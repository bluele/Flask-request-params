#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup, find_packages
from os.path import dirname, abspath, join, isfile
import platform

cwd = abspath(dirname(__file__))
version = platform.python_version()
install_requires = []


def install_requirements():
    req_path = join(cwd, 'requirements.txt')
    if isfile(req_path):
        with open(req_path) as f:
            mods = filter(lambda m: len(m) > 0, f.read().split('\n'))
        install_requires.extend(mods)


def read_file(filename):
    path = join(cwd, filename)
    if isfile(path):
        return open(path).read()


install_requirements()


setup(
    name='Flask-request-params',
    version='0.1.0',
    description="Rails like interface for HTTP Request parameter of Flask.",
    long_description=read_file('README.rst'),
    license='MIT',
    author='bluele',
    author_email='jksmphone@gmail.com',
    url='https://github.com/bluele/flask-request-params',
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Environment :: Console',
    'Topic :: System :: Shells',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.6',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3.3',
    ],
    include_package_data=True,
    packages=find_packages(),
    keywords='flask',
    install_requires=install_requires,
    zip_safe=False
)
