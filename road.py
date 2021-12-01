from turtle import Turtle


class Road(Turtle):
    def __init__(self):
        super().__init__()
        self.pencolor("white")
        self.hideturtle()
        self.pensize(3)
        self.penup()
        self.goto(300, 250)
        self.pendown()
        self.backward(600)
        self.penup()
        self.goto(300, -250)
        self.pendown()
        self.backward(600)
        self.y_pos = 225
        self.pencolor("yellow")
        for _ in range(19):
            self.penup()
            self.goto(305, self.y_pos)
            for _ in range(30):
                self.pendown()
                self.backward(20)
                self.penup()
                self.backward(20)
            self.y_pos -= 25




