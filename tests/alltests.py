import unittest,os
from ctypes import *

app_path = os.path.dirname(os.path.abspath(__file__))
libpathname = os.path.join(app_path, "./libled.so")
led = CDLL(libpathname);

verbose = 0

def boslog(msg):
    global verbose
    if verbose:
        print msg

def led_monitor_value():
    return c_uint.in_dll(led, "_led")

class BOSTest_led(unittest.TestCase):

    def test_turn_onoff(self):
        '''
        void led_turn_on(unsigned int c);
        void led_turn_off(unsigned int c);
        '''
        led.turn_on()
        v = led.get_value();
        print "after turnon %x" % v
        assert v == 1, "led should be off"

        # alternative way to get _led value
        print "%x" % led_monitor_value().value;

        led.turn_off()

        v = led.get_value();
        print "after turnoff %x" % v
        assert v == 0, "led should be on"

def suite_led():
    bosTestSuite = unittest.makeSuite(BOSTest_led, 'test')
    return bosTestSuite

def main():
    suite1 = suite_led()
    alltests = unittest.TestSuite((suite1))
    runner = unittest.TextTestRunner()
    runner.run(alltests);

if __name__ == "__main__":
    main()
