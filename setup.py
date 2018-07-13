#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=6.0', 'regex','requests>=2.19.1','bs4>=0.0.1']

setup_requirements = [ ]

test_requirements = [ ]

setup(
    author="Tyler F.",
    author_email='tyfal647@gmail.com',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    description="RPython package that utilizes requests and regex to make digging through the SEC database eand analyzing 10 forms easy.",
    entry_points={
        'console_scripts': [
            'tenform=tenform.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tenform',
    name='tenform',
    packages=find_packages(include=['tenform','utils']),
    setup_requires=setup_requirements,
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/tyfal/tenform',
    version='0.1.4',
    zip_safe=False,
)
