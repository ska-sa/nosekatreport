# Copyright (c) 2013 National Research Foundation (South African Radio Astronomy Observatory)
# BSD license - see LICENSE for details
from setuptools import setup, find_packages


setup(
    name='nosekatreport',
    description='Nose plugin for writing an annotated test report',
    long_description=open('README.rst').read(),
    author='cam',
    author_email='cam@ska.ac.za',
    license='BSD',
    packages=find_packages(exclude=['ez_setup']),
    install_requires=['Nose>=0.11.0', 'traceback2', 'ansicolors', 'numpy'],
    url='',
    include_package_data=True,
    entry_points="""
        [nose.plugins.0.10]
        nosekatreport = nosekatreport:KatReportPlugin
        """,
    classifiers = [
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Testing',
        'Topic :: Software Development :: Documentation'
        ],
)
