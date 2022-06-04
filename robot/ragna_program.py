#!/usr/bin/env python3

# importing the project specific robot classes
import robot.models as models

from adafruit_motor import servo
from adafruit_pca9685 import PCA9685

# diverse imports for board and coding managment
from board import SCL, SDA
import busio

# setting up the i2c bus
i2c = busio.I2C(SCL, SDA)

# setting up the two pwm controllers with corresponding address
controllerLeft = PCA9685(i2c,address = 0x40)
controllerRight = PCA9685(i2c,address = 0x41)

controllerLeft.frequency = 50
controllerRight.frequency = 50

# initializing all robot legs
leftFrontLeg = models.Leg(
        [servo.Servo(controllerLeft.channels[0], min_pulse = 800, max_pulse = 2450),
         servo.Servo(controllerLeft.channels[1], min_pulse = 800, max_pulse = 2450),
         servo.Servo(controllerLeft.channels[2], min_pulse = 800, max_pulse = 2450)])

leftBackLeg = models.Leg(
        [servo.Servo(controllerLeft.channels[13], min_pulse = 800, max_pulse = 2450),
         servo.Servo(controllerLeft.channels[14], min_pulse = 800, max_pulse = 2450),
         servo.Servo(controllerLeft.channels[15], min_pulse = 800, max_pulse = 2450)])

rightFrontLeg = models.Leg(
        [servo.Servo(controllerRight.channels[13], min_pulse = 800, max_pulse = 2450),
         servo.Servo(controllerRight.channels[14], min_pulse = 800, max_pulse = 2450),
         servo.Servo(controllerRight.channels[15], min_pulse = 800, max_pulse = 2450)])

rightBackLeg = models.Leg(
        [servo.Servo(controllerRight.channels[0], min_pulse = 800, max_pulse = 2450),
         servo.Servo(controllerRight.channels[1], min_pulse = 780, max_pulse = 2450),
         servo.Servo(controllerRight.channels[2], min_pulse = 800, max_pulse = 2450)])

# initializing robot
robot = models.Robot(leftFrontLeg,leftBackLeg,rightFrontLeg,rightBackLeg)
