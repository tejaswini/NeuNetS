#!/usr/bin/env python
'''Set up file for AutoNN Package'''
from setuptools import find_packages, setup

setup(name='ibm_neunets_processor',
      version='0.5',
      description='Python library to inference on trained neunets models',
      author='IBM',
      author_email='',
      url='https://github.com/pmservice/NeuNetS/neunets_processor',
      packages=find_packages(),
      install_requires=["numpy==1.15.4", "Pillow==5.3.0", "scikit-image"],
      dependency_links=[])
