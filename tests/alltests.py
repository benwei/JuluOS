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


class BOSTest_led(unittest.TestCase):
    def test_turn_onoff(self):
        '''
        const char *led_turn_on(unsigned char c);
        '''
        led.turn_on(c_char(0))
        assert led._led == 0, "led should be off"
	led.turn_off(c_char(1))
        assert led._led == 0, "led should be on"

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
