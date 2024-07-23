import turtle
import random
import time

delay=0.1
score = 0
high_score = 0

# Creating the window and setting height and width
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("black")
wn.setup(width=700, height=700)
wn.tracer(0)

#Creating a border for the game
turtle.speed(5)
turtle.pensize(4)
turtle.penup()
turtle.goto(-310,250)
turtle.pendown()
turtle.color('black')
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.right(90)
turtle.forward(600)
turtle.right(90)
turtle.forward(500)
turtle.penup()
turtle.hideturtle()

# Crerating head of the snake
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


#Creating food in the game
food = turtle.Turtle()
food_color = random.choice(['yellow', 'green', 'tomato'])
food_shape = random.choice([ 'triangle', 'circle','square'])
food.speed(0)
food.shape(food_shape)
food.color(food_color)
food.penup()
food.goto(20, 20)

#Creating space to show score and high score
scoreBoard = turtle.Turtle()
scoreBoard.speed(0)
scoreBoard.shape("square")
scoreBoard.color("white")
scoreBoard.penup()
scoreBoard.hideturtle()
scoreBoard.goto(0, 250)
scoreBoard.write("Score : 0 High Score : 0", align="center",
        font=("Courier", 25, "bold"))


# assigning key directions
def move_up():
    if head.direction != "down":
        head.direction = "up"


def move_down():
    if head.direction != "up":
        head.direction = "down"


def move_left():
    if head.direction != "right":
        head.direction = "left"


def move_right():
    if head.direction != "left":
        head.direction = "right"


def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y+20)
    if head.direction == "down":
        y = head.ycor()
        head.sety(y-20)
    if head.direction == "left":
        x = head.xcor()
        head.setx(x-20)
    if head.direction == "right":
        x = head.xcor()
        head.setx(x+20)


wn.listen()
wn.onkeypress(move_up, "Up")
wn.onkeypress(move_down, "Down")
wn.onkeypress(move_left, "Left")
wn.onkeypress(move_right, "Right")

segments = []

# Main Game
while True: #Running an infinite till the collision occurs and then game ends
    wn.update()

    #Ending the game on collision with any of the walls
    if head.xcor() > 280 or head.xcor() < -300 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)
        wn.bgcolor('blue')
        scoreBoard.goto(0,0)
        scoreBoard.write("GAME OVER\n Your Score is : {}".format(
            score), align="center", font=("Courier", 30, "bold"))

    #If snake collects food
    if head.distance(food) < 20:
        #increasing score and updating the high_score if required
        score += 10
        if score > high_score:
            high_score = score
        scoreBoard.clear()
        scoreBoard.write("Score : {} High Score : {} ".format(
            score, high_score), align="center", font=("Courier", 25, "bold"))

        #creating food at random location
        x_cord = random.randint(-290, 270)
        y_cord = random.randint(-240, 240)
        food_color = random.choice(['yellow', 'green', 'tomato'])
        food_shape = random.choice([ 'triangle', 'circle','square'])
        food.speed(0)
        food.shape(food_shape)
        food.color(food_color)
        food.goto(x_cord, y_cord)

        # Adding a new segment to the snake
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white smoke") # giving a new color to the tail
        new_segment.penup()
        segments.append(new_segment) #adding the segment to the list

        
    # Moving the snake and ending the game on collisions of head with body segments
    for i in range(len(segments)-1, 0, -1):
        x = segments[i-1].xcor()
        y = segments[i-1].ycor()
        segments[i].goto(x, y)
    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x, y)
    move()

    #Checking for collision with the body
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            wn.clear()
            wn.bgcolor('blue')
            scoreBoard.goto(0,0)
            scoreBoard.write("\t\tGAME OVER\n Your Score is : {}".format(
                score), align="center", font=("Courier", 30, "bold"))

    time.sleep(delay)

turtle.Terminator()
