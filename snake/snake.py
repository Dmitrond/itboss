import turtle
import random

WIDTH = 500
HEIGHT = 500
FOOD_SISE = 10
Score = 1

def draw_borders():
    p = turtle.Pen()
    p.penup()
    p.goto(-WIDTH/2, HEIGHT/2)
    p.pendown()
    p.goto(-WIDTH / 2, -HEIGHT / 2)
    p.goto(WIDTH / 2, -HEIGHT / 2)
    p.goto(WIDTH / 2, HEIGHT / 2)
    p.goto(-WIDTH / 2, HEIGHT / 2)
    p.penup()
    p.hideturtle()


def generate_food_pos():
    x = random.randint(-WIDTH / 2 + FOOD_SISE, WIDTH / 2 - FOOD_SISE)
    y = random.randint(-HEIGHT / 2 + FOOD_SISE, HEIGHT / 2 - FOOD_SISE)
    return x, y

def draw_snake():
    for segment in snake:
        t.goto(segment[0], segment[1]) # segment = [0, 0]
        t.stamp()

def draw_score(score):
    t.clear()
    t.goto(0, HEIGHT / 2 + 20)
    t.write(f"Score: {score}", align="center", font=("Courier", 24, "normal"))

def move_snake():
    global snake_direction, score
    if collision():
        reset()
    else:
        t.clearstamps()
        if not food_collision():
            snake.pop(0)
        else:
            score = score + Score
            draw_score(score)
        if snake_direction == "right":
            snake.append([snake[-1][0] + 20, snake[-1][1]])
        elif snake_direction == "left":
            snake.append([snake[-1][0] - 20, snake[-1][1]])
        elif snake_direction == "up":
            snake.append([snake[-1][0], snake[-1][1] + 20])
        elif snake_direction == "down":
            snake.append([snake[-1][0], snake[-1][1] - 20])

        draw_snake()
        screen.update()
        turtle.ontimer(move_snake, 200)

def go_left():
    global snake_direction
    if snake_direction !=  "right":
        snake_direction = "left"

def go_right():
    global snake_direction
    if snake_direction !=  "left":
        snake_direction = "right"

def go_up():
    global snake_direction
    if snake_direction !=  "down":
        snake_direction = "up"

def go_down():
    global snake_direction
    if snake_direction !=  "up":
        snake_direction = "down"

def get_distance(pos1, pos2):
    x1, y1 = pos1
    x2, y2 = pos2
    return ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5


def food_collision():
    global food_pos
    if get_distance(snake[-1], food_pos) < 20:
        food_pos = generate_food_pos()
        food.goto(food_pos)
        return True
    return False
def collision():
    global snake
    head_x = snake[-1][0]
    head_y = snake[-1][1]

    if head_x > WIDTH / 2 - 10 or head_x < - WIDTH / 2 + 10:
        return True
    if head_y > HEIGHT / 2 - 10 or head_y < - HEIGHT / 2 + 10:
        return True
    if snake[-1] in snake[:-1]:
        return True
    return False

def reset():
    global snake, snake_direction, food_pos, score
    snake = [[0, 0], [20, 0], [40, 0], [60, 0]]
    score = 0
    draw_score(score)
    draw_borders()
    draw_snake()
    food_pos = generate_food_pos()
    food.goto(food_pos)
    snake_direction = "right"
    move_snake()

screen = turtle.Screen()
screen.tracer(0)

t = turtle.Turtle("square")
t.penup()

food = turtle.Turtle("circle")
food.color("red")
food.penup()




screen.listen()
screen.onkey(go_left, "Left")
screen.onkey(go_right, "Right")
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")

reset()
turtle.done()






































