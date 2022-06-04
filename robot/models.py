from gpiozero import LED
import math
import time

# initialising GPIO17 as LED
led = LED(17)

class Leg:

    # alpha = firstServo | beta = secondServo | gamma = for calculation purpouses | delta = shoulderServo | alphaMin = for fwd and bwd movement
    
    servos = []
    length = 0
    alpha = 0
    alphaMin = 90
    beta = 0
    gamma = 0
    delta = 0

    def __init__(self,servos,length = 135):
        self.servos = servos
        self.length = length
        led.on()

    def moveUp(self):
        # dont change alphaMin
        # set a fixed height, calculate angles and move servos accordingly
        upperPosition = 30
        self.calculateByHeight(upperPosition)
        self.moveServos()

    def moveDown(self):
        # dont change alphaMin
        # set a fixed height, calculate angles and move servos accordingly
        lowerPosition = 150
        self.calculateByHeight(lowerPosition)
        self.moveServos()

    def moveForward(self):
        # set alphaMin smaller to move leg forward
        # all basic angles stay the same
        pass
    
    def moveBackwards(self):
        # set alphaMin higher to move leg backwards
        # all basic angles stay the same
        pass

    def moveToOriginal(self):
        # set alphaMin to 90 to move Leg back to standard positon
        # all basic angles stay the same
        pass

    def calculateByHeight(self, height):
        self.height = height
        self.alpha = (math.acos((self.height**2 + self.length**2 - self.length**2) / (2 * self.height * self.length))) / ( math.pi / 180)
        self.beta  = (math.acos((self.length**2 + self.length**2 - self.height**2) / (2 * self.length * self.length))) / ( math.pi / 180)
        self.gamma = (math.acos((self.length**2 + self.height**2 - self.length**2) / (2 * self.length * self.height))) / ( math.pi / 180)

    def moveServos(self,direction):
        if direction == "right":
            self.servos[1].angle = 180 - (self.alpha + self.alphaMin)
            self.servos[2].angle = 180 - self.beta
        if direction == "left":
            self.servos[1].angle = self.alpha + self.alphaMin
            self.servos[2].angle = self.beta

class Robot:
    
    name = 'Ragna'

    leftFrontLeg: Leg = None
    leftBackLeg: Leg = None
    rightFrontLeg: Leg = None
    rightBackLeg: Leg = None

    def __init__(self,leftFrontLeg,leftBackLeg,rightFrontLeg,rightBackLeg):
        self.leftFrontLeg = leftFrontLeg
        self.leftBackLeg = leftBackLeg
        self.rightFrontLeg = rightFrontLeg
        self.rightBackLeg = rightBackLeg
    
    def turnLeft(self):
        pass

    def turnRight(self):
        pass

    def moveLeft(self):
        pass

    def moveRight(self):
        pass

    def moveForward(self):
        self.leftFrontLeg.moveUp()
        time.sleep(1)
        self.leftFrontLeg.moveDown()

    def moveBackwards(self):
        pass

    def sit(self):
        pass

    def standUp (self):
        self.leftFrontLeg.calculateByHeight(200)
        self.leftBackLeg.calculateByHeight(200)
        self.rightFrontLeg.calculateByHeight(200)
        self.rightBackLeg.calculateByHeight(200)

        self.leftFrontLeg.moveServos("left")
        self.leftBackLeg.moveServos("left")
        self.rightFrontLeg.moveServos("right")
        self.rightBackLeg.moveServos("right")

    def layDown(self):
        self.leftFrontLeg.servos[1].angle = 180
        self.leftFrontLeg.servos[2].angle = 180
        self.leftBackLeg.servos[1].angle = 180
        self.leftBackLeg.servos[2].angle = 180
        self.rightFrontLeg.servos[1].angle = 180 - 180
        self.rightFrontLeg.servos[2].angle = 180 - 180
        self.rightBackLeg.servos[1].angle = 180 - 180
        self.rightBackLeg.servos[2].angle = 180 - 180

    def wiggle(self):
        # only move shoudler Servos 
        # try to make it walk side
        pass
    