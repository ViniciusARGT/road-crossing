from turtle import Turtle
import random

COLORS = ["red", "orange", "white", "brown", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.car_list = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle(shape="square")
            car.penup()
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.goto(300, random.randrange(-238, 238, 25))
            self.car_list.append(car)

    def move(self):
        for car_n in self.car_list:
            car_n.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
