import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
screen.listen()
screen.onkey(player.goup,"Up")
carmanager=CarManager()
scoreboard=Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(.07)
    screen.update()
    carmanager.cars()
    carmanager.move()
    if player.ycor() > 290:
        player.win()
        carmanager.levelup()
        scoreboard.levelupp()

    for car in carmanager.allCars:
        if car.distance(player) < 20:
            scoreboard.gameover()
            time.sleep(5)
            game_is_on =False

