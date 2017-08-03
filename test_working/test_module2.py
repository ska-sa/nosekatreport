###############################################################################
# SKA South Africa (http://ska.ac.za/)                                        #
# Author: cam@ska.ac.za                                                       #
# Copyright @ 2013 SKA SA. All rights reserved.                               #
#                                                                             #
# THIS SOFTWARE MAY NOT BE COPIED OR DISTRIBUTED IN ANY FORM WITHOUT THE      #
# WRITTEN PERMISSION OF SKA SA.                                               #
###############################################################################
"""A battery of tests for Shiney Module 2"""
import unittest

from nosekatreport import report_subpass, satisfies_requirement


class TestResiliency(unittest.TestCase):
    """Abuse a shiney module2 to test resiliency."""
    @satisfies_requirement('M2Bend10')
    def test_bending_ten_times(self):
        """Bend the shiney module2 object ten times and check functioning afterwards."""
        self.assertTrue(True)
        report_subpass('Bending module2 left')
        self.assertTrue(True)
        report_subpass('Bending module2 right')

    def test_bashing_twenty_times(self):
        """Bash shiney module2 object twenty times and check functioning afterwards."""
        self.assertTrue(True)
        report_subpass('Counting slowly after bashing module2')
        self.assertEqual(['onee', 'two', 'three'], ['one', 'two', 'three'],
                         msg='module2 failed counting test after twenty bashes')
        report_subpass('Counting fast after bashing')


class TestFunction(unittest.TestCase):
    """Test proper functioning of a fresh shiney module2"""
    @satisfies_requirement('M2FCslow')
    @satisfies_requirement('MilSTDCount2')
    def test_counting_slowly(self):
        """Test if shiney module2 object count slowly and correctly"""
        self.assertTrue(True)
        report_subpass('Slow numerical counting module2')
        self.assertTrue(True)
        report_subpass('Fast numerical  counting module2')

    @satisfies_requirement('M2FCfast')
    def test_counting_fast(self):
        """Test if shiney module2 object count fast and correctly"""
        self.assertEqual([1,2,3,4], range(1,5))
        report_subpass('Fast numerical counting module2')
        self.assertEqual(['one', 'too', 'three', 'four'],
                         ['one', 'two', 'three', 'four'],
                         msg='Incorrect textual fast counting')
        report_subpass('Fast textual counting module2')
