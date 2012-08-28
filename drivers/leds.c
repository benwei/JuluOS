#include "leds.h"

#define MAX_LEDS 10

unsigned int _leds[MAX_LEDS];

int 
turn_on(unsigned int num)
{
	if (num > MAX_LEDS-1)
		return -1;

	_leds[num] = 1;
}

int
turn_off(unsigned int num)
{
	if (num > MAX_LEDS-1)
		return -1;

	_leds[num] = 0;
}

unsigned int
get_value(unsigned int num)
{
	return _leds[num];
}

