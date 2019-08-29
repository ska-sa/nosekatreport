###############################################################################
# SKA South Africa (http://ska.ac.za/)                                        #
# Author: cam@ska.ac.za                                                       #
# Copyright @ 2013 SKA SA. All rights reserved.                               #
#                                                                             #
# THIS SOFTWARE MAY NOT BE COPIED OR DISTRIBUTED IN ANY FORM WITHOUT THE      #
# WRITTEN PERMISSION OF SKA SA.                                               #
###############################################################################
import sys
import unittest2 as unittest

from tests import intrusive, fixtures, wait_with_strategy
from nosekatreport import report_subfail, satisfies_requirement, report_progress

class TestTemplate(unittest.TestCase):
    """This is a template class to start building kat system tests with."""

    def setUp(self):
        self.cam = fixtures.cam
        self.sim = fixtures.sim

    @intrusive
    def test_intrusive(self):
        """An intrusive test"""

        report_progress("Running an intrusive test")
        it_passed = True
        self.assertTrue(it_passed, msg='Oh my goodness, it FAILED!!!!')

    @unittest.skipIf(1 == 1, "Testing skipIf always")
    def test_skipif(self):
        """Test skipIf"""
        if False:                         #Uh-oh, this should not happen
            report_subfail("This should have been skipped")

    @unittest.expectedFailure
    def test_expected_failure(self):
        """Test expected failure"""
        self.assertTrue(False, "This is an expected failure")

    @unittest.skipIf(sys.version_info < (2, 6),
                     "not supported in this veresion")
    def test_skip_if_not_2_6(self):
        # testing some things here
        report_progress("Version is >= 2.6")


