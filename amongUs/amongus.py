import turtle
print("What color would you like your crewmate to be?")
print("Enter the number: ")
print("\n1. Red,\n2. Blue,\n3. Green,\n4. Yellow,\n5. Orange,\n6. Black,\n7. White,\n8. Purple,\n9. Cyan,\n10. Brown,\n11. Lime, \n12. Grey, \n13. Fortegreen")

color = int(input("Enter the number: "))
if color == 1:
    BODY_COLOR = 'red'
elif color == 2:
    BODY_COLOR = 'blue'
elif color == 3:
    BODY_COLOR = 'green'
elif color == 4:
    BODY_COLOR = 'yellow'
elif color == 5:
    BODY_COLOR = 'orange'
elif color == 6:
    BODY_COLOR = 'black'
elif color == 7:
    BODY_COLOR = 'white'
elif color == 8:
    BODY_COLOR = 'purple'
elif color == 9:
    BODY_COLOR = 'cyan'
elif color == 10:
    BODY_COLOR = 'brown'
elif color == 11:
    BODY_COLOR = 'lime'
elif color == 12:
    BODY_COLOR = 'grey'
elif color == 13:
    BODY_COLOR = 'forest green'
else:
    print("Not valid")


BODY_SHADOW = ''
GLASS_COLOR = '#9acedc'
GLASS_SHADOW = ''

t = turtle.Turtle()

# it can move forward backward left right


def body():
    """ draws the body """
    t.pensize(20)
    # t.speed(15)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    # right side
    t.right(90)
    t.forward(50)
    t.right(180)
    t.circle(40, -180)
    t.right(180)
    t.forward(200)

    # head curve
    t.right(180)
    t.circle(100, -180)

    # left side
    t.backward(20)
    t.left(15)
    t.circle(500, -20)
    t.backward(20)

    # t.backward(200)
    t.circle(40, -180)
    # t.right(90)
    t.left(7)
    t.backward(50)

    # hip
    t.up()
    t.left(90)
    t.forward(10)
    t.right(90)
    t.down()
    # t.right(180)
    #t.circle(25, -180)
    t.right(240)
    t.circle(50, -70)

    t.end_fill()


def glass():
    t.up()
    # t.right(180)
    t.right(230)
    t.forward(100)
    t.left(90)
    t.forward(20)
    t.right(90)

    t.down()
    t.fillcolor(GLASS_COLOR)
    t.begin_fill()

    t.right(150)
    t.circle(90, -55)

    t.right(180)
    t.forward(1)
    t.right(180)
    t.circle(10, -65)
    t.right(180)
    t.forward(110)
    t.right(180)

    # t.right(180)
    t.circle(50, -190)
    t.right(170)
    t.forward(80)

    t.right(180)
    t.circle(45, -30)

    t.end_fill()


def backpack():
    t.up()
    t.right(60)
    t.forward(100)
    t.right(90)
    t.forward(75)

    t.fillcolor(BODY_COLOR)
    t.begin_fill()

    t.down()
    t.forward(30)
    t.right(255)

    t.circle(300, -30)
    t.right(260)
    t.forward(30)

    t.end_fill()


def hat():
    t.up()
    t.forward(100)
    t.left(100)
    t.forward(125)
    t.down()
    t.forward(25)


body()
glass()
backpack()
hat()
