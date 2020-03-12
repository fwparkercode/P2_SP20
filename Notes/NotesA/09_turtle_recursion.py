# Turtle recursion
import turtle

my_turtle = turtle.Turtle()
my_turtle.shape("classic")
my_turtle.speed(0)

my_screen = turtle.Screen()
my_screen.bgcolor('white')
my_screen.setup(width=800, height=800, startx=0, starty=0)


# draw a shape using goto
my_turtle.fillcolor('red')
my_turtle.begin_fill()  # starts a shape to fill in
my_turtle.goto(200, 0)
my_turtle.goto(200, 200)
my_turtle.goto(0, 200)
my_turtle.goto(0, 0)
my_turtle.end_fill()

# pick up the turtle
my_turtle.up()
my_turtle.goto(-200, -200)
my_turtle.down()
my_turtle.fillcolor('blue')
my_turtle.begin_fill()
my_turtle.goto(0, 0)
my_turtle.goto(0, -200)
my_turtle.goto(-200, -200)
my_turtle.end_fill()

# draw using headings
my_turtle.up()
my_turtle.goto(0,0)
my_turtle.down()
my_turtle.width(4)

my_turtle.fillcolor('yellow')
my_turtle.begin_fill()
my_turtle.setheading(90)  # turtle heading to North

for i in range(12):
    my_turtle.forward(50)
    my_turtle.left(30)
my_turtle.end_fill()


# Recursive rectangle pattern
my_screen.clear()
my_turtle.home()

def recursive_rect(width, height, depth):
    if depth > 0:
        my_turtle.width(depth)
        my_turtle.up()
        my_turtle.goto(width / 2, height / 2)  # top right
        my_turtle.down()
        my_turtle.goto(width / 2, -height / 2)  # bottom right
        my_turtle.goto(-width / 2, - height / 2)  # bottom left
        my_turtle.goto(-width / 2, height / 2)  # top left
        my_turtle.goto(width / 2, height / 2)
        recursive_rect(width / 1.5, height / 1.5, depth - 1)

recursive_rect(800, 500, 10)


my_screen.clear()
my_turtle.home()

def ncaa(x, y, width, height, depth):
    if depth > 0:
        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()  # start drawing

        # draw top
        my_turtle.goto(x, y + height / 2)
        my_turtle.goto(x + width, y + height / 2)

        my_turtle.up()
        my_turtle.goto(x, y)
        my_turtle.down()  # start drawing

        # draw bottom
        my_turtle.goto(x, y - height / 2)
        my_turtle.goto(x + width, y - height / 2)

        ncaa(x + width, y + height / 2, width, height / 2, depth - 1)
        ncaa(x + width, y - height / 2, width, height / 2, depth - 1)

ncaa(-300, 0, 100, 280, 6)


my_screen.exitonclick()

