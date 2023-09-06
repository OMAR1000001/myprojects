from turtle import Turtle
import random


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.allCars=[]
        self.NEW_START=STARTING_MOVE_DISTANCE
    def cars(self):
        rando= random.randint(1,6)
        if rando ==1:
            new_car=Turtle("square")
            new_car.shapesize(.5,1)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            randomY=random.randint(-250,200)
            new_car.goto(300,randomY)
            self.allCars.append(new_car)

    def move(self):
        for movecars in self.allCars:
            movecars.backward(self.NEW_START)

    def levelup(self):
        self.NEW_START += MOVE_INCREMENT