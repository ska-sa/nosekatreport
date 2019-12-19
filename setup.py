# Copyright (c) 2017 National Research Foundation (South African Radio Astronomy Observatory)
# BSD license - see LICENSE for details
from __future__ import absolute_import, division, print_function

from os import path
from setuptools import setup, find_packages

this_directory = path.abspath(path.dirname(__file__))
files = {"Readme": "README.rst"}
long_description = ""
for name, filename in files.items():
    long_description = "{}{}\n".format(long_description, name)
    with open(path.join(this_directory, filename)) as f:
        file_contents = f.read()
    long_description = "{}{}\n\n".format(long_description, file_contents)

setup(
    name="nosekatreport",
    description="Nose plugin for writing an annotated test report",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="cam",
    author_email="cam@ska.ac.za",
    license="BSD",
    packages=find_packages(exclude=["ez_setup"]),
    url="https://github.com/ska-sa/nosekatreport/",
    include_package_data=True,
    entry_points="""
        [nose.plugins.0.10]
        nosekatreport = nosekatreport:KatReportPlugin
        """,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Natural Language :: English",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python",
        "Topic :: Software Development :: Documentation",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
    ],
    platforms=["OS Independent"],
    keywords="meerkat kat ska",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, !=3.3.*, !=3.4.*",
    setup_requires=["katversion"],
    use_katversion=True,
    install_requires=[
        "future",
        "futures; python_version<'3'",
        "Nose>=0.11.0",
        "traceback2",
        "ansicolors",
        "numpy",
    ],
    zip_safe=False,
    test_suite="nose.collector",
)
