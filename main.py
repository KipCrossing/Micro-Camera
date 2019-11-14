import os
import camera
import machine
import time


led = machine.Pin(4, machine.Pin.OUT)


def run(tfile):
    camera.init()
    led.on()
    time.sleep(0.5)
    buf = camera.capture()
    led.off()
    camera.deinit()
    print(buf[0:8])
    f = open(tfile, 'wb')
    f.write(buf)
    f.close()


numf = open('number.txt', 'r')
num = 1
for i in numf:
    num = i
    print(num)
numf.close()

run('sd/Image'+str(num)+'.jpg')

numf = open('number.txt', 'w')
numf.write(str(int(num)+1))
numf.close()
