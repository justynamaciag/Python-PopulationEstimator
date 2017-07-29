#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='PopulationEstimator',
    version='0.1.6',
    description="Population",
    long_description=readme + '\n\n' + history,
    author="Justyna Maciąg",
    author_email='justynamaciag96@gmail.com',
    url='https://github.com/justynamaciag/PopulationEstimator',
    packages=[
        'PopulationEstimator',
    ],
    package_dir={'PopulationEstmiator':
                 'PopulationEstimator'},
    entry_points={
        'console_scripts': [
            'PopulationEstimator=PopulationEstimator.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="GNU General Public License v3",
    zip_safe=False,
    keywords='PopulationEstimator',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
