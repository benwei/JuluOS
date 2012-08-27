CFILES= ../drivers/led.c
CFLAGS+=-I ../inc

OBJS=$(CFILES:.c=.o)
LIBLED_SHARED = libled.so

all: $(LIBLED_SHARED)
	python alltests.py

%.o :%.c
	$(CC) -c $< -o $@ $(CFLAGS) $(INCS)

$(LIBLED_SHARED): $(OBJS)
	$(CC) -shared -o $@ $^

clean:
	rm -f *.so $(OBJS)
