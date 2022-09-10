# -*- coding: utf-8 -*-
################################################################################
#                                  arancia                                     #
################################################################################
import setuptools

with open("requirements.txt") as f:
    required_packages = f.read().splitlines()

setuptools.setup(
    name="network-science",
    version="0.1.0",
    author="Fernando Carazo",
    author_email="fernando.carazom@gmail.com",
    description="Functions to analyze Networks. Based on the book Network Science - Abert Barabasi.",
    # install_requires=required_packages,
    packages=setuptools.find_packages(),
)
