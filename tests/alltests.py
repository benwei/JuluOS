import unittest,os
from ctypes import *

app_path = os.path.dirname(os.path.abspath(__file__))
libpathname = os.path.join(app_path, "./libleds.so")
leds = CDLL(libpathname);

verbose = 0

def boslog(msg):
    global verbose
    if verbose:
        print msg

class BOSTest_leds(unittest.TestCase):

    def test_turn_onoff(self):
        '''
        void leds_turn_on(unsigned int c);
        void leds_turn_off(unsigned int c);
        '''
        leds.turn_on(c_uint(9))
        v = leds.get_state(c_uint(9));
        print "after turnon %x" % v
        assert v == 1, "led 9 should be off"


        v = leds.get_state(c_uint(0));
        assert v == 0, "led 0 should be off"

        leds.turn_off(c_uint(9))

    def test_turn_outbound(self):
        r = leds.turn_on(c_uint(100))
        assert r == -1, "led 100 not existed"


def suite_leds():
    bosTestSuite = unittest.makeSuite(BOSTest_leds, 'test')
    return bosTestSuite

def main():
    suite1 = suite_leds()
    alltests = unittest.TestSuite((suite1))
    runner = unittest.TextTestRunner()
    runner.run(alltests);

if __name__ == "__main__":
    main()
