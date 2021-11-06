from turtle import Turtle, Screen
Move_Distance = 20
Up = 90
Down = 270
Left = 180
Right = 0

s = Screen()


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        x = 0
        y = 0
        for i in range(3):
            new_snake = Turtle()
            new_snake.penup()
            new_snake.shape("square")
            new_snake.color("white")
            new_snake.ht()
            new_snake.setposition(x, y)
            self.segments.append(new_snake)
            x -= 20

        for snake_part in self.segments:
            snake_part.st()

    def up(self):
        if self.head.heading() != Down:
            self.head.setheading(Up)

    def down(self):
        if self.head.heading() != Up:
            self.head.setheading(Down)

    def left(self):
        if self.head.heading() != Right:
            self.head.setheading(Left)

    def right(self):
        if self.head.heading() != Left:
            self.head.setheading(Right)

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[i - 1].xcor()
            new_y = self.segments[i - 1].ycor()
            self.segments[i].goto(new_x, new_y)
        self.head.forward(Move_Distance)

    def grow(self):
        prev_x = self.segments[-1].xcor()
        prev_y = self.segments[-1].ycor()
        new_snake = Turtle()
        new_snake.shape("square")
        new_snake.color("white")
        new_snake.penup()
        new_snake.ht()
        new_snake.setposition(prev_x - 20, prev_y)
        self.segments.append(new_snake)
        new_snake.st()

    def reset(self):
        for seg in self.segments:
            seg.goto(2000, 2000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]



