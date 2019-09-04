from __future__ import (absolute_import, division, print_function)

from future import standard_library
standard_library.install_aliases()

import unittest
from builtins import str

# Copyright (c) 2017 National Research Foundation (South African Radio Astronomy Observatory)
# BSD license - see LICENSE for details
from nosekatreport import (Aqf, aqf_vr, intrusive, site_acceptance, site_only, slow,
                           system,  StoreTestRun, KatReportPlugin)
from nosekatreport.plugin import _state


@system('all')
class TestAqf(unittest.TestCase):

    """Tests AQF decorators."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    @aqf_vr('VR.EXAMPLE.FC.4', 'VR.EXAMPLE.FC.6', 'VR.EXAMPLE.FC.9', 'CBF-REQ-0126',
            'CBF-REQ-0047', 'TP.C.1.19')
    def test_aqf_decorators(self):
        Aqf.hop()
        Aqf.step("Setup")
        #Aqf.sensor('sim.sensors.asc_wind_speed').get()
        # Set something on the simulator.
        Aqf.stepBold("Bold Setup")
        Aqf.stepline("Underlined Step")
        Aqf.wait(1)
        value_from_sensor = 10
        Aqf.equals(10, value_from_sensor,
                   'Test that the sensor has a value of 10')
        Aqf.more(11, value_from_sensor,
                 "Test that the sensor has a value more than 10")
        Aqf.less(6, value_from_sensor,
                 "Test that the sensor has a value less than 10")
        Aqf.step("Set elevation limits")
        min_ap_elevation = 15.0
        max_ap_elevation = 90.0
        Aqf.in_range(30, min_ap_elevation, max_ap_elevation,
                     "Check if result falls within expected limits")
        Aqf.step("Check that result has a value almost equal")
        Aqf.almost_equals(10.2, value_from_sensor, 0.5,
                          "Test that the sensor has an almost equal value to 10")
        Aqf.step("Give Minimum and Maximum Limits for AP Elevation")
        Aqf.array_almost_equal([15, 90], [min_ap_elevation, max_ap_elevation],
                               "Check max and min elevation")
        Aqf.step("Check is system in on.")
        system_on = True
        Aqf.is_true(system_on, 'Check that the system_on switch is set.')
        Aqf.step("Read the first message from the system.")
        ## Your Code here.
        message = 'hallo world'
        Aqf.equals('hallo world', message,
                   'Check that "hallo world" is returned.')
        message = 'Hello world'
        Aqf.is_not_equals('hallo world', message,
                          'Check that "hallo world" is returned.')
        Aqf.step('Open KatGUI and observe sensors')
        Aqf.checkbox('On the sensor display and observe that there are sensors')
        Aqf.step("Switch off.")
        Aqf.skipped("Skipped. We cannot switch the system off at the moment.")
        Aqf.step("Log into KatGUI")
        Aqf.keywait("Press Enter to continue")
        Aqf.step("Test TBD.")
        Aqf.waived("This next task has been waived")
        Aqf.tbd("TBD. Still to do test.")
        Aqf.wait(2, "Wait to proccess next step")
        Aqf.step("Add line at end of the test")
        linewidth = 100
        Aqf.addLine('_', linewidth)
        Aqf.end()

    @aqf_vr('VR.EXAMPLE.FC.6')
    @aqf_vr('VR.EXAMPLE.FC.15', 'VR.EXAMPLE.FC.16')
    def test_aqf_decorators_2(self):
        Aqf.step("Make sure the sensor give us a status.")
        Aqf.progress("Get status from sensor")
        # Your code here.
        status = True
        Aqf.is_true(status, "Check that sensor status is true")
        Aqf.waived("This next task has been waived")
        Aqf.tbd("TBD. Still to do test.")
        Aqf.wait(2, "Wait to proccess next step")
        Aqf.step("Set the value of the sensor")
        Aqf.step('Open KatGUI and observe sensors')
        Aqf.checkbox('On the sensor display and observe that there are sensors')
        # Your code here.
        status = False
        Aqf.is_false(status, "Check that the sensor status is now false")
        # Aqf.failed("Test failed")
        Aqf.end()

    @unittest.skip('CAM to implement')
    @intrusive
    @aqf_vr('VR.CM.EXAMPLE.17')
    def test_aqf_decorators_3(self):
        Aqf.step("Setup")

        s = Aqf.sensor('sim.sensors.asc_wind_speed').get()
        Aqf.progress("The2 sensor was %s" % str(s))
        Aqf.sensor('sim.sensors.asc_wind_speed').set(10)
        s = Aqf.sensor('sim.sensors.asc_wind_speed').get()
        Aqf.progress("The3 sensor was %s" % str(s))
        Aqf.sensor('sim.sensors.asc_wind_speed').set(33, 1, 2)
        s = Aqf.sensor('sim.sensors.asc_wind_speed').get()
        Aqf.progress("The3 sensor was %s" % str(s))
        Aqf.sensor("cam.m063.sensor.rsc_rsc_vac_pump_running").get()
        Aqf.waived("This next task has been waived")
        Aqf.tbd("TBD. Still to do test.")
        Aqf.wait(2, "Wait to proccess next step")
        Aqf.step('Open KatGUI and observe sensors')
        Aqf.checkbox('On the sensor display and observe that there are sensors')
        Aqf.end()

@system('all')
class TestStoreTestRun(unittest.TestCase):

    def setUp(self):
        self.storerun = StoreTestRun()

    def tearDown(self):
        pass

    def test_test_name(self):
        self.assertEqual(self.storerun.test_name, 'Unknown')


@system('all')
class Test_state(unittest.TestCase):
    def setUp(self):
        self._state = _state()

    def tearDown(self):
        pass

    def test_store_run(self):
        self.assertTrue(isinstance(self._state.store, StoreTestRun))
