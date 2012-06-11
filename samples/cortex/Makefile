
# semihosting cannot be run qemu with cortex-m3, qemu encountered segmentation fault right away
# qemu verion QEMU emulator version 0.14.0 (qemu-kvm-0.14.0
# Ubuntu 11.04 32bit
MCPU=cortex-m3

MCPU=cortex-a8
QEMU_EXTRA=-cpu $(MCPU) 

ifneq ($(MCPU),cortex-m3)
ARCH_FLAGS=-mcpu=$(MCPU) -mthumb 
QEMU_EXTRA+=-semihosting 
else
ARCH_FLAGS=-mcpu=$(MCPU) -mthumb 
#USEGDB=
endif

CROSSCOMPILE=/opt/arm-2012.03/bin/arm-none-eabi-
CC=$(CROSSCOMPILE)gcc
LD=$(CROSSCOMPILE)ld
AS=$(CROSSCOMPILE)as
OBJCOPY=$(CROSSCOMPILE)objcopy
OBJDUMP=$(CROSSCOMPILE)objdump

OUTPUT=kernel.elf kernel.bin

OBJS=kernel.o

all: $(OUTPUT)

.c.o:
	$(CC) -c $< -g

kernel.elf: $(OBJS)
	$(CC) -o $@ $^ $(ARCH_FLAGS) -T generic-hosted.ld

kernel.bin: kernel.elf
	$(OBJCOPY) -O binary $^ $@

dump: kernel.elf
	$(OBJDUMP) -d $^ > kernel.asm
	

clean:
	rm -f *.o $(OUTPUT) kernel.asm

qemu: kernel.bin
	@if [ "0$(USEGDB)" -eq 1 ]; then \
	echo "use gdb" ; \
	QEMUCMD="qemu-system-arm  -singlestep $(QEMU_EXTRA) -nographic -monitor null -serial null -semihosting -kernel kernel.bin -gdb tcp::51234" ; \
	else \
	QEMUCMD="qemu-system-arm  $(QEMU_EXTRA) -nographic -monitor null -serial null -kernel kernel.bin" ; \
	fi ; \
	echo "$$QEMUCMD" ; \
	$$QEMUCMD

