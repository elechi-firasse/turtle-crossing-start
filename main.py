import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
car_manager = CarManager()

game_is_on = True
screen.listen()
screen.onkey(player.move_up, "Up")

while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()
    if player.level_pass():
        scoreboard.level_up()
        car_manager.STARTING_MOVE_DISTANCE +=














screen.exitonclick()


