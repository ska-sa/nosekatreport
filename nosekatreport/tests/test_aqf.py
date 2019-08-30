# Copyright (c) 2013 National Research Foundation (South African Radio Astronomy Observatory)
# BSD license - see LICENSE for details
import unittest

from nosekatreport import (Aqf, aqf_vr, system, slow, intrusive,
                           site_only, site_acceptance)


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
        Aqf.step("Check is system in on.")
        system_on = True
        Aqf.is_true(system_on, 'Check that the system_on switch is set.')
        Aqf.step("Read the first message from the system.")
        ## Your Code here.
        message = 'hallo world'
        Aqf.equals('hallo world', message,
                   'Check that "hallo world" is returned.')
        Aqf.step("Switch off.")
        Aqf.skipped("Skipped. We cannot switch the system off at the moment.")
        Aqf.step("Test TBD.")
        Aqf.tbd("TBD. Still to do test.")
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
        Aqf.step("Set the value of the sensor")
        # Your code here.
        status = False
        Aqf.is_false(status, "Check that the sensor status is now false")
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

        Aqf.step('Open KatGUI and observe sensors')
        Aqf.checkbox('On the sensor display and observe that there are sensors')
        Aqf.end()


if __name__ == '__main__':
    unittest.main()
