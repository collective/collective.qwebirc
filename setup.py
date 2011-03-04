
from setuptools import find_all, setup

setup(
    version='1.0',
    name='collective.qwebirc',
    packages=find_all(),
    namespace_packages=['collective'],
    install_requires='Twisted'
)
