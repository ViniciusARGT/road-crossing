import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road import Road


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Road Crossing")

screen.tracer(0)
road = Road()
turtle = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(turtle.up, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create()
    car.move()

    for cars in car.car_list:
        if cars.distance(turtle) < 20:
            scoreboard.game_over()
            game_is_on = False

    if turtle.finish_line():
        turtle.new_level()
        car.level_up()
        scoreboard.increase_level()
        scoreboard.update_scoreboard()

screen.exitonclick()