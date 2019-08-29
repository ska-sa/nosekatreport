###############################################################################
# SKA South Africa (http://ska.ac.za/)                                        #
# Author: cam@ska.ac.za                                                       #
# Copyright @ 2013 SKA SA. All rights reserved.                               #
#                                                                             #
# THIS SOFTWARE MAY NOT BE COPIED OR DISTRIBUTED IN ANY FORM WITHOUT THE      #
# WRITTEN PERMISSION OF SKA SA.                                               #
###############################################################################
from setuptools import setup, find_packages


setup(
    name="nosekatreport",
    version="0.3",
    description="Nose plugin for writing an annotated test report.",
    long_description=open("README.rst").read(),
    author="CAM team",
    author_email="cam@ska.ac.za",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    install_requires=["Nose>=0.11.0", "traceback2", "ansicolors", "numpy"],
    setup_requires=["katversion"],
    use_katversion=True,
    url="http://ska.ac.za/",
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
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Documentation",
    ],
    platforms=["OS Independent"],
    python_requires=">=2.7, !=3.0.*, !=3.1.*, !=3.2.*, <4",
    test_suite="nose.collector",
)
