import sys
import time

# setting path
sys.path.append('..')

from typing import Union
from fastapi import FastAPI
import robot.ragna_program as ragna

app = FastAPI()

# start and stop logic of forward movement
@app.get("/move_forward_start")
def read_root():
    ragna.robot.moveForward()
    return {}

@app.get("/move_forward_stop")
def read_root():
    ragna.robot.buttonState = 0
    return {}

# start and stop logic of backwards movement
@app.get("/move_backwards_start")
def read_root():
    ragna.robot.moveBackwards()
    return {}

@app.get("/move_backwards_stop")
def read_root():
    ragna.robot.buttonState = 0
    return {}

# start and stop logic of turning right movement
@app.get("/turn_right_start")
def read_root():
    ragna.robot.turnRight()
    return {}

@app.get("/turn_right_stop")
def read_root():
    ragna.robot.buttonState = 0
    return {}    

# start and stop logic of turning left movement
@app.get("/turn_left_start")
def read_root():
    ragna.robot.turnLeft()
    return {}

@app.get("/turn_left_stop")
def read_root():
    ragna.robot.buttonState = 0
    return {}

# start and stop logic of sideways right movement
@app.get("/move_right")
def read_root():
    ragna.robot.moveRight()
    return {}

@app.get("/move_right_stop")
def read_root():
    ragna.robot.buttonState = 0
    return {}

# start and stop logic of sideways left movement
@app.get("/move_left_start")
def read_root():
    ragna.robot.moveLeft()
    return {}

@app.get("/move_left_stop")
def read_root():
    ragna.robot.buttonState = 0
    return {}

# one time movements
@app.get("/sit")
def read_root():
    ragna.robot.sit()
    return {}

@app.get("/standUp")
def read_root():
    ragna.robot.standUp()
    return {}

@app.get("/layDown")
def read_root():
    ragna.robot.layDown()
    return {}

@app.get("/wiggle")
def read_root():
    ragna.robot.wiggle()
    return {}