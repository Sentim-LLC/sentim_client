# coding: utf-8

"""
    Sentim's Emotion APIs

    An emotion recognition api that tells you the emotion of text, and not just the connotation.  # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Contact: help@sentimllc.com
    Generated by: https://openapi-generator.tech
"""


from setuptools import setup, find_packages  # noqa: H301

NAME = "sentim_api"
VERSION = "1.0.0"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["urllib3 >= 1.15", "six >= 1.10", "certifi", "python-dateutil"]

setup(
    name=NAME,
    version=VERSION,
    description="Sentim&#39;s Emotion APIs",
    author_email="help@sentimllc.com",
    url="",
    keywords=["OpenAPI", "OpenAPI-Generator", "Sentim's Emotion APIs"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "tests"]),
    include_package_data=True,
    long_description="""\
    An emotion recognition api that tells you the emotion of text, and not just the connotation.  # noqa: E501
    """
)