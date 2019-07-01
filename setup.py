#!/usr/bin/env python
# -*- encoding: utf-8 -*-

from setuptools import setup

setup(
    name='Elodie Plus',
    version='1.0.0',
    description='Your Personal EXIF-based Photo, Video and Audio Assistant.',
    url='https://github.com/lancelotj/elodie.git',
    author='Lance',
    author_email='mail@gmail.com',
    license='MIT',
    include_package_data=True,
    packages=['elodie'],
    install_requires=[
        'click==6.6',
        'requests==2.20.0',
        'Send2Trash==1.3.0',
        'future==0.16.0',
        'configparser==3.5.0',
        'tabulate==0.7.7',
    ],
    entry_points='''
        [console_scripts]
        elodie=elodie.elodie:main
    ''',
)
