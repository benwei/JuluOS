#include "leds.h"

unsigned int _leds[10];

void
turn_on(unsigned int num)
{
	_leds[num] = 1;
}

void
turn_off(unsigned int num)
{
	_leds[num] = 0;
}


unsigned int
get_value(unsigned int num)
{
	return _leds[num];
}

