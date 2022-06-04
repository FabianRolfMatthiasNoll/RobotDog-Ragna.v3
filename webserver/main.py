import sys

# setting path
sys.path.append('..')

from typing import Union
from fastapi import FastAPI
import robot.ragna_program as ragna

app = FastAPI()

@app.get("/move_forward")
def read_root():
    ragna.robot.moveForward()
    return {}

@app.get("/move_backwards")
def read_root():
    ragna.robot.moveBackwards()
    return {}

@app.get("/turn_Right")
def read_root():
    ragna.robot.turnRight()
    return {}

@app.get("/turn_Left")
def read_root():
    ragna.robot.turnLeft()
    return {}

@app.get("/move_Right")
def read_root():
    ragna.robot.moveRight()
    return {}

@app.get("/move_Left")
def read_root():
    ragna.robot.moveLeft
    return {}

@app.get("/sit")
def read_root():
    ragna.robot.sit
    return {}

@app.get("/standUp")
def read_root():
    ragna.robot.standUp
    return {}

@app.get("/layDown")
def read_root():
    ragna.robot.layDown
    return {}

@app.get("/wiggle")
def read_root():
    ragna.robot.wiggle
    return {}