from setuptools import setup

setup(
    name = 'label-fast',
    version = '0.1.1',
    packages = ['cli'],
    entry_points = {
        'console_scripts': [
            'lf = cli.main:main'
        ]
    })
