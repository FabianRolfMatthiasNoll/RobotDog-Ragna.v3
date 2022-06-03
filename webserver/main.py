import sys

# setting path
sys.path.append('..')

from typing import Union

from fastapi import FastAPI

import robot.ragna_program as ragna

app = FastAPI()

@app.get("/move")
def read_root():
    ragna.leftFrontLeg.moveUp()

    ragna.time.sleep(1)

    ragna.leftFrontLeg.moveDown()

    return {}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}