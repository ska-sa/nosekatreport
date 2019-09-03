from __future__ import (absolute_import, division, print_function,
                        unicode_literals)

# Copyright (c) 2017 National Research Foundation (South African Radio Astronomy Observatory)
# BSD license - see LICENSE for details
from future import standard_library
from setuptools import find_packages, setup

standard_library.install_aliases()


setup(
    name="nosekatreport",
    description="Nose plugin for writing an annotated test report",
    long_description=open("README.rst").read(),
    author="cam",
    author_email="cam@ska.ac.za",
    license="BSD",
    packages=find_packages(exclude=["ez_setup"]),
    url="",
    include_package_data=True,
    entry_points="""
        [nose.plugins.0.10]
        nosekatreport = nosekatreport:KatReportPlugin
        """,
    classifiers=[
        "Development Status :: 2 - Pre-Alpha",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: GNU General Public License (GPL)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.5",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Documentation"
        ],
    platforms=["OS Independent"],
    keywords="meerkat kat ska",
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4",
    setup_requires=["katversion"],
    use_katversion=True,
    install_requires=[
        "elasticsearch>=5.4.0",
        "future",
        "futures; python_version<'3'",
        "katconf",
        "tornado>=4.3, <5.0; python_version<'3'",
        "tornado>=4.3, <7.0; python_version>='3'",
        "Nose>=0.11.0", "traceback2",
        "ansicolors", "numpy"
    ],
    zip_safe=False,
    test_suite="nose.collector",
)
