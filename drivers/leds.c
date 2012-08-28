#include "leds.h"

unsigned int _leds;

void
turn_on(void)
{
	_leds = 1;
}

void
turn_off(void)
{
	_leds = 0;
}


unsigned int
get_value(void)
{
	return _leds;
}

