#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
  name = "run",
  packages = find_packages(),
  entry_points = {
    "console_scripts": [
      "run = run:main",
    ]
  }
)

