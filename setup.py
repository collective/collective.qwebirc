
from setuptools import find_packages, setup

setup(
    version='1.0',
    name='collective.qwebirc',
    packages=find_packages(),
    namespace_packages=['collective'],
    install_requires=[
        'Twisted',
        'setuptools'
    ],
    entry_point="""
    [z3c.autoinclude.plugin]
    target = plone
    """
)
