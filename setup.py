#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages
import io
import os.path

README = \
'''
Adapt google assistant's gRPC sample app for working with respeakerd
'''

def samples_requirements():
    with io.open('requirements.txt') as f:
        for p in f:
            yield p.strip()

requirements = list(samples_requirements())

setup_requirements = [
    # TODO: put setup requirements (distutils extensions, etc.) here
]

test_requirements = [
    'pytest'
]

setup(
    name='googleassistant_respeakerd',
    version='0.1.2',
    description=README,
    long_description=README,
    author="Jack Shao",
    author_email='jacky.shaoxg@gmail.com',
    url='https://github.com/respeaker/googleassistant_respeakerd',
    packages=find_packages(include=['googleassistant_respeakerd']),
    include_package_data=True,
    install_requires=requirements,
    entry_points={
        'console_scripts': [
            'googlesamples-assistant-respeakerd=googleassistant_respeakerd.assist_with_respeakerd:main'
        ],
    },
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='google assistant, respeaker',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    setup_requires=setup_requirements,
)
