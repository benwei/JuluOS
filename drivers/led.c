#include "led.h"

unsigned int _led;

void
turn_on(void)
{
	_led = 1;
}

void
turn_off(void)
{
	_led = 0;
}


unsigned int
get_value(void)
{
	return _led;
}

