"""Distribution setup."""

import os

from setuptools import setup

with open("README.rst", "r") as fh:
    long_description = fh.read()


setup(
    name="NasaFloater",
    description=long_description,
    packages=[],
    install_requires=[
        "orbit-nrel==1.0.5",
        "jupyterlab",
        "seaborn"
    ],
)
