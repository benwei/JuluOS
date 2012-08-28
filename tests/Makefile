CFILES= ../drivers/leds.c
CFLAGS+=-I ../inc

OBJS=$(CFILES:.c=.o)
LIBLED_SHARED = libleds.so

all: $(LIBLED_SHARED)
	python alltests.py

%.o :%.c
	$(CC) -c $< -o $@ $(CFLAGS) $(INCS)

$(LIBLED_SHARED): $(OBJS)
	$(CC) -shared -o $@ $^

clean:
	rm -f *.so $(OBJS)
