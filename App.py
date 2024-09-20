import turtle
import random

color_list = [(132, 164, 203), (228, 150, 99), (31, 44, 64), (166, 57, 47), (201, 136, 148), (237, 212, 87),
              (44, 101, 146), (136, 182, 161), (149, 63, 72), (161, 33, 31), (58, 48, 45), (51, 41, 44), (59, 116, 100),
              (230, 164, 169), (237, 166, 155), (170, 30, 32), (217, 83, 72), (36, 61, 55), (15, 97, 70), (34, 60, 107),
              (170, 187, 221), (196, 100, 108), (14, 86, 110), (107, 126, 158), (35, 150, 210), (175, 199, 189)]


def random_color():
    red = random.randint(0, 255)
    blue = random.randint(0, 255)
    green = random.randint(0, 255)
    return red, green, blue


def random_color_from_list():
    return random.choice(color_list)


def clear_screen():
    tim.penup()
    tim.home()
    tim.clear()
    tim.pendown()


"""Turtle set up"""
turtle.colormode(255)
tim = turtle.Turtle()
tim.speed(0)
tim_screen = tim.getscreen()
tim.pensize(10)
SCREEN_WIDTH = tim_screen.window_width() / 2
SCREEN_HEIGHT = tim_screen.window_height() / 2
BOTTOM_LEFT_X = -SCREEN_WIDTH + 255
BOTTOM_LEFT_Y = -SCREEN_HEIGHT + 180


def many_shapes():
    """Draws many shapes"""
    for shape_sides in range(3, 11):
        tim.color(random_color())
        for _ in range(shape_sides):
            angle = 360 / shape_sides
            tim.forward(100)
            tim.right(angle)


def random_walk():
    """Draws an imitation of the random walk"""
    directions = {
        "forward": tim.forward,
        "back": tim.back,
        "left": [tim.left, tim.forward],
        "right": [tim.right, tim.forward],
    }
    for _ in range(100):
        direction = random.choice(list(directions.keys()))
        tim.color(random_color())
        if direction == "left" or direction == "right":
            directions[direction][0](90)
            directions[direction][1](30)
        else:
            directions[direction](30)


def circles():
    """Draws mandala of circles"""
    angle = 5
    size_of_gap = int(360 / angle)
    for _ in range(size_of_gap):
        tim.color(random_color())
        tim.circle(100)
        tim.right(angle)


def dot_painting():
    """Draws dot painting"""
    new_ycor = BOTTOM_LEFT_Y
    for row in range(10):
        tim.goto(BOTTOM_LEFT_X, new_ycor)
        for col in range(10):
            tim.dot(20, random_color_from_list())
            tim.forward(50)
        new_ycor += 50
        tim.goto((BOTTOM_LEFT_X, new_ycor))


def etch_sketch():
    """Lets you draw whatever you want, with a,w,s,d keys to move, like etch sketch"""

    def move_forwards():
        tim.forward(10)

    def move_backwards():
        tim.back(10)

    def rotate_left():
        tim.left(10)

    def rotate_right():
        tim.right(10)

    tim_screen.onkey(fun=move_forwards, key="w")
    tim_screen.onkey(fun=move_backwards, key="s")
    tim_screen.onkey(fun=rotate_left, key="a")
    tim_screen.onkey(fun=rotate_right, key="d")
    tim_screen.onkey(fun=clear_screen, key="c")
    tim_screen.listen()
    tim_screen.exitonclick()


def turtle_race():
    """Turtles racing from one side of the screen to the other, you guess at the beginning who might win, the first turtle to cross the finish line is announced"""
    screen = turtle.Screen()
    turtle.TurtleScreen._RUNNING = True
    screen.setup(width=500, height=400)
    user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
    colors = ["red", "orange", "yellow", "green", "blue", "purple"]
    turtle_list = []
    start_x_position = -230
    start_y_position = -70
    is_race_on = False
    if user_bet:
        is_race_on = True

    for color in colors:
        turtle_tempo = turtle.Turtle(shape="turtle")
        turtle_tempo.penup()
        turtle_tempo.color(color)
        turtle_tempo.goto(x=start_x_position, y=start_y_position)
        turtle_list.append(turtle_tempo)
        start_y_position += 30

    while is_race_on:
        for turtle_tempo in turtle_list:
            random_dist = random.randint(0, 10)
            turtle_tempo.forward(random_dist)
            if turtle_tempo.xcor() >= 230:  # tim.pensize(2)
                winning_color = turtle_tempo.pencolor()
                is_race_on = False
                if winning_color == user_bet.lower():
                    print(f"You've won! the {winning_color} turtle is the winner!")
                else:
                    print(f"You've lost! the {winning_color} turtle is the winner!")
                break
    screen.exitonclick()


if __name__ == "__main__":
    many_shapes()
    clear_screen()
    random_walk()
    clear_screen()
    tim.penup()
    dot_painting()
    clear_screen()
    tim.pensize(2)
    circles()
    clear_screen()
    tim.color("black")
    etch_sketch()
    turtle_race()
