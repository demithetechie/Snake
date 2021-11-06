from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import pandas as pd
import time

# setting up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

# # animation control
# screen.tracer(0)
#
# # Object creation
# s = Snake()
# f = Food()
# score = ScoreBoard()
#
# # Controlling the snake
# screen.onkeypress(s.up, "Up")
# screen.onkeypress(s.down, "Down")
# screen.onkeypress(s.left, "Left")
# screen.onkeypress(s.right, "Right")
# screen.listen()
# GameOn = True


def SnakeGame():
    # animation control
    screen.tracer(0)

    # Object creation
    s = Snake()
    f = Food()
    score = ScoreBoard()

    # Controlling the snake
    screen.onkeypress(s.up, "Up")
    screen.onkeypress(s.down, "Down")
    screen.onkeypress(s.left, "Left")
    screen.onkeypress(s.right, "Right")
    screen.listen()
    game_on = True
    while game_on:
        screen.update()
        s.move()

        # Detect collision with snake and food
        if s.head.distance(f) < 15:
            s.grow()
            f.refresh()
            score.increment_score()

        # Detect collision with wall
        if s.head.xcor() > 280 or s.head.xcor() < -280 or s.head.ycor() > 280 or s.head.ycor() < -280:
            game_on = False
            score.reset()
            s.reset()
            score.game_over()

        # Detect collision with tail
        for segment in s.segments[1:]:
            if s.head.distance(segment) < 10:
                game_on = False
                score.reset()
                s.reset()
                score.game_over()
        time.sleep(0.1)
    # name = screen.textinput("First name", "Enter your name for the leaderboard")
    # final_score = score.high_score
    # high_scores = {
    #     name: final_score
    # }
    # highscore_data = pd.DataFrame(high_scores)
    # highscore_data.to_csv("highscores.csv")

    replay = screen.textinput("Play again?", "Would you like to play again? Type 'y' for yes, and 'n' for no.")
    if replay == 'y':
        screen.clear()
        SnakeGame()
    else:
        screen.clear()

    screen.exitonclick()


SnakeGame()