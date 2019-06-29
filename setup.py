from setuptools import setup, find_packages

setup(
    name='Elodie Plus',
    version='0.1',
    description='Phrase and article analyzer',
    url='https://github.com/lancelotj/elodie.git',
    author='Lance',
    author_email='mail@gmail.com',
    license='MIT',
    include_package_data=True,
    py_modules=['elodie'],
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
        elodie=elodie:main
    ''',
)
