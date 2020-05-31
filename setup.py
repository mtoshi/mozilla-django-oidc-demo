# -*- coding: utf-8 -*-
"""setup."""

from setuptools import setup
from setuptools import find_packages


requires = []
with open('requirements.txt', 'w') as _file:
    _file.write('\n'.join(requires))

setup(
    name='mozilla-django-oidc-demo',
    version='0.0.3',
    url='https://github.com/mtoshi/mozilla-django-oidc-demo',
    author='mtoshi',
    author_email='mtoshi@outlook.com',
    description='Experimental app.',
    packages=find_packages(),
    install_requires=requires,
)
