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
    alphaMin = 100
    beta = 0
    gamma = 0
    delta = 0
    alphaCorrection = 0 
    betaCorrection = 0
    omegaCorrection = 0 # Shoulder Servo Correction

    def __init__(self,servos,length = 110):
        self.servos = servos
        self.length = length
        led.on()

    def moveUp(self, direction):
        # dont change alphaMin
        # set a fixed height, calculate angles and move servos accordingly
        upperPosition = 30
        self.calculateByHeight(upperPosition)
        self.moveServos(direction)

    def moveDown(self, direction):
        # dont change alphaMin
        # set a fixed height, calculate angles and move servos accordingly
        lowerPosition = 150
        self.calculateByHeight(lowerPosition)
        self.moveServos(direction)

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
        self.alpha = ((math.acos((self.height**2 + self.length**2 - self.length**2) / (2 * self.height * self.length))) / ( math.pi / 180)) - self.alphaCorrection - 7
        self.beta  = ((math.acos((self.length**2 + self.length**2 - self.height**2) / (2 * self.length * self.length))) / ( math.pi / 180)) - self.betaCorrection
        self.gamma = ((math.acos((self.length**2 + self.height**2 - self.length**2) / (2 * self.length * self.height))) / ( math.pi / 180))
        if(self.beta < 40): self.beta = 50

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
    buttonState = 1

    def __init__(self,leftFrontLeg,leftBackLeg,rightFrontLeg,rightBackLeg):
        self.leftFrontLeg = leftFrontLeg
        self.leftBackLeg = leftBackLeg
        self.rightFrontLeg = rightFrontLeg
        self.rightBackLeg = rightBackLeg

        # Angle Correction Values
        self.leftFrontLeg.alphaCorrection = 0
        self.leftFrontLeg.betaCorrection = 0
        self.leftFrontLeg.omegaCorrection = -7

        self.leftBackLeg.alphaCorrection = 0
        self.leftBackLeg.betaCorrection = -10
        self.leftBackLeg.omegaCorrection = -7

        self.rightFrontLeg.alphaCorrection = -(0)
        self.rightFrontLeg.betaCorrection = -(0)
        self.rightFrontLeg.omegaCorrection = -(-7)

        self.rightBackLeg.alphaCorrection = -(-5)
        self.rightBackLeg.betaCorrection = -(0)
        self.rightBackLeg.omegaCorrection = -(0)

        self.standUp()
    
    def turnLeft(self):
        pass
        #while self.buttonState == 1:
        #    self.leftFrontLeg.moveUp("left")
        #    time.sleep(1)
        #    self.leftFrontLeg.moveDown("left")
        #    time.sleep(1)
        #self.buttonState = 1

    def turnRight(self):
        pass

    def moveLeft(self):
        self.leftFrontLeg.servos[2].angle += 5
        self.rightFrontLeg.servos[2].angle -= 5
        self.leftBackLeg.servos[2].angle += 5
        self.rightBackLeg.servos[2].angle -= 5

    def moveRight(self):
        self.leftFrontLeg.servos[2].angle -= 5
        self.rightFrontLeg.servos[2].angle += 5
        self.leftBackLeg.servos[2].angle -= 5
        self.rightBackLeg.servos[2].angle += 5

    def moveForward(self):
        pass

    def moveBackwards(self):
        pass

    def sit(self):
        self.leftFrontLeg.servos[0].angle = 90 - self.leftFrontLeg.omegaCorrection
        self.rightFrontLeg.servos[0].angle = 90 - self.rightFrontLeg.omegaCorrection
        self.leftBackLeg.servos[0].angle = 90 - self.leftBackLeg.omegaCorrection
        self.rightBackLeg.servos[0].angle = 90 - self.rightBackLeg.omegaCorrection

        self.leftFrontLeg.servos[1].angle = 90 - self.leftFrontLeg.alphaCorrection
        self.rightFrontLeg.servos[1].angle = 90 - self.rightFrontLeg.alphaCorrection
        self.leftBackLeg.servos[1].angle = 90 - self.leftBackLeg.alphaCorrection
        self.rightBackLeg.servos[1].angle = 90 - self.rightBackLeg.alphaCorrection

        self.leftFrontLeg.servos[2].angle = 90 - self.leftFrontLeg.betaCorrection
        self.rightFrontLeg.servos[2].angle = 90 - self.rightFrontLeg.betaCorrection
        self.leftBackLeg.servos[2].angle = 90 - self.leftBackLeg.betaCorrection
        self.rightBackLeg.servos[2].angle = 90 - self.rightBackLeg.betaCorrection

    def straightenShoulders (self):
        self.leftFrontLeg.servos[0].angle = 90 - self.leftFrontLeg.omegaCorrection
        self.rightFrontLeg.servos[0].angle = 90 - self.rightFrontLeg.omegaCorrection
        self.leftBackLeg.servos[0].angle = 90 - self.leftBackLeg.omegaCorrection
        self.rightBackLeg.servos[0].angle = 90 - self.rightBackLeg.omegaCorrection    

    def standUp (self):
        self.leftFrontLeg.calculateByHeight(180)
        self.leftBackLeg.calculateByHeight(180)
        self.rightFrontLeg.calculateByHeight(180)
        self.rightBackLeg.calculateByHeight(180)

        self.leftFrontLeg.moveServos("left")
        self.leftBackLeg.moveServos("left")
        self.rightFrontLeg.moveServos("right")
        self.rightBackLeg.moveServos("right")

    def layDown(self):
        
        self.leftFrontLeg.servos[2].angle = 65
        self.leftBackLeg.servos[2].angle = 65
        self.rightFrontLeg.servos[2].angle = 180 - 65
        self.rightBackLeg.servos[2].angle = 180 - 65

        self.leftFrontLeg.servos[1].angle = 160
        self.leftBackLeg.servos[1].angle = 160
        self.rightFrontLeg.servos[1].angle = 180 - 160
        self.rightBackLeg.servos[1].angle = 180 - 160

        time.sleep(0.2)

        self.leftFrontLeg.servos[2].angle = 40
        self.leftBackLeg.servos[2].angle = 40
        self.rightFrontLeg.servos[2].angle = 180 - 40
        self.rightBackLeg.servos[2].angle = 180 - 40

        time.sleep(0.2)

        self.leftFrontLeg.servos[1].angle = 180
        self.leftBackLeg.servos[1].angle = 180
        self.rightFrontLeg.servos[1].angle = 180 - 180
        self.rightBackLeg.servos[1].angle = 180 - 180
        
        
    def wiggle(self):
        # only move shoudler Servos 
        # try to make it walk side
        pass
    