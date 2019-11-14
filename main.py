import os
import camera
import machine
import time


led = machine.Pin(4, machine.Pin.OUT)

w = 12
if w > 0 or w < 13:
    camera.framesize(w)
w = 63
if w > 9 or w < 64:
    camera.quality(w)


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

'''
w = -111
if w > 0 or w < 13:
    camera.framesize(w)
if w > 9 or w < 64:
    camera.quality(w)
if w > -3 or w < 3:
    camera.contrast(w)
if w > -3 or w < 3:
    camera.saturation(w)
if w > -3 or w < 3:
    camera.brightness(w)
if w >= 0 or w < 7:
    camera.speffect(w)
if w >= 0 or w < 5:
    camera.whitebalance(w)
'''
