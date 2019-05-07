# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='pyshella-toolkit',
    version='0.30.1',
    description='BTC/fork hack toolkit.',
    author='mkbeh',
    license='MIT',
    platforms='any',
    install_requires=[
        'aiobitcoin',
        'uvloop',
        'aiofiles'
    ],
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'pyshella-scanner = src.cli_scanner:cli',
            'pyshella-cw = src.cli_cw:test'
        ],
    },
)
