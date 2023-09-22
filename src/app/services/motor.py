import time

from app.library.Threading import Threading
from app.library.VsWrc201 import I2CMotor
from app.library.SharedMemory import Queue

SpeedQueue = Queue("/speedPoint")

@Threading().run()
def motor():
    I2CMotor.init()
    useable_speed = 0
    while True:
        speed = SpeedQueue.receive_non_block()
        if speed:
            useable_speed = speed
        I2CMotor.drive_motor(-int(useable_speed), int(useable_speed))

@Threading().run()
def speed():
    while True:
        for x in range(70, 80, 1):
            SpeedQueue.send(str(x))
            time.sleep(1)

