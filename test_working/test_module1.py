###############################################################################
# SKA South Africa (http://ska.ac.za/)                                        #
# Author: cam@ska.ac.za                                                       #
# Copyright @ 2013 SKA SA. All rights reserved.                               #
#                                                                             #
# THIS SOFTWARE MAY NOT BE COPIED OR DISTRIBUTED IN ANY FORM WITHOUT THE      #
# WRITTEN PERMISSION OF SKA SA.                                               #
###############################################################################
"""A battery of tests for Shiney Module 1"""
import unittest2 as unittest
from nosekatreport import report_subpass, satisfies_requirement


class TestResiliency(unittest.TestCase):
    """Abuse a shiney module1 to test resiliency."""
    @satisfies_requirement('M1Bend10')
    def test_bending_ten_times(self):
        """Bend shiney object ten times and check functioning afterwards."""
        self.assertTrue(True)
        report_subpass('Bending left')
        self.assertTrue(True)
        report_subpass('Bending right')

    def test_bashing_twenty_times(self):
        """Bash shiney object twenty times and check functioning afterwards."""
        self.assertTrue(True)
        report_subpass('Counting slowly after bashing')
        self.assertEqual(['one', 'two', 'thee'], ['one', 'two', 'three'],
                         msg='module1 failed counting test after twenty bashes')
        report_subpass('Counting fast after bashing')


class TestFunction(unittest.TestCase):
    """Test proper functioning of a fresh shiney module1"""
    @satisfies_requirement('M1FCslow')
    @satisfies_requirement('MilSTDCount1')
    def test_counting_slowly(self):
        """Test if shiney object count slowly and correctly"""
        self.assertTrue(True)
        report_subpass('Slow numerical counting')
        self.assertTrue(True)
        report_subpass('Fast numerical  counting')

    @satisfies_requirement('M1FCfast')
    def test_counting_fast(self):
        """Test if shiney object count fast and correctly"""
        self.assertEqual([1,2,3,4], range(1,5))
        report_subpass('Fast numerical counting')
        self.assertEqual(['one', 'two', 'three', 'fwor'],
                         ['one', 'two', 'three', 'four'],
                         msg='Incorrect textual fast counting')
        report_subpass('Fast textual counting')
