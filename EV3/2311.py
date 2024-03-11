#!/usr/bin/env pybricks-micropython
import time

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile
from pybricks import ev3brick as brick

# This program requires LEGO EV3 MicroPython v2.0 or higher.
# Click "Open user guide" on the EV3 extension tab for more information.


# Create your objects here.
ev3 = EV3Brick()


# Write your program here.
# ev3.speaker.beep()


# Play a sound.
brick.sound.beep()
# Initialize a motor at port B.
test_motor = Motor(Port.B)
test_motor.
# test_motor1 = Motor(Port.A)
# Run the motor up to 500 degrees per second. To a target angle of 90 degrees.
test_motor.run_target(500, 360)
# test_motor1.run_target(500, 1000)
# Play another beep sound.
# This time with a higher pitch(1000 Hz) and longer duration(500 ms).
# Make the light red
brick.light(Color.RED)
brick.sound.beep(1000, 500)
test_touch = UltrasonicSensor(Port.S1)

time.sleep(10)
while True:
    if flag:
        test_motor1.