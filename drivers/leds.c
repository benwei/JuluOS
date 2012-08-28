#include "leds.h"

#define MAX_LEDS 10

unsigned int _leds[MAX_LEDS];

#define IF_OUTBOUND_THEN_RETURN_NONE_ZERO(num) { \
	if (num > MAX_LEDS-1) \
		return -1; \
}

int 
turn_on(unsigned int num)
{
	IF_OUTBOUND_THEN_RETURN_NONE_ZERO(num);

	_leds[num] = 1;
	return 0;
}

int
turn_off(unsigned int num)
{
	IF_OUTBOUND_THEN_RETURN_NONE_ZERO(num);

	_leds[num] = 0;
	return 0;
}

int
get_state(unsigned int num)
{
	IF_OUTBOUND_THEN_RETURN_NONE_ZERO(num);
	return _leds[num];
}

