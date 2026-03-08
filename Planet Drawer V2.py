from turtle import *

def draw_square(color):
    ti.pendown()
    ti.color('gray',color)
    ti.begin_fill()
    for i in range(4):
        ti.forward(40)
        ti.left(90)
    ti.end_fill()
    ti.penup()

def draw_triangle(color):
    ti.pendown()
    ti.color('gray',color)
    ti.begin_fill()
    for i in range(3):
        ti.forward(40)
        ti.left(120)
    ti.end_fill()
    ti.penup()

def draw_star(color):
    ti.pendown()
    ti.color('gray',color)
    ti.begin_fill()
    for i in range(5):
        ti.forward(40)
        ti.left(100)
    ti.end_fill()
    ti.penup()

def draw_symbol(symbol, indent):
    ti.forward(indent)
    ti.pendown()
    ti.color('gray')
    ti.write(symbol, font=("Arial",12,"normal"))
    ti.penup()

def circle_t(size):
    ti.pendown()
    ti.begin_fill()
    ti.color('gray')
    ti.circle(size)
    ti.end_fill()
    ti.penup()

def draw(x, y):
    t.goto(x, y)

def move(x, y):
    t.penup()
    t.goto(x, y)
    t.pendown()

def red():
    t.color("red")

def orange():
    t.color("orange")

def yellow():
    t.color("yellow")

def green():
    t.color("green")

def blue():
    t.color("blue")

def indigo():
    t.color("indigo")

def violet():
    t.color("violet")

def black():
    t.color("black")

def white():
    t.color("white")

def abu():
    t.color("gray")

def thickone():
    t.width(5)

def thicktwo():
    t.width(10)

def thickthree():
    t.width(15)

def thickfour():
    t.width(20)

def thickfive():
    t.width(25)

def thicksix():
    t.width(30)

def thickseven():
    t.width(35)

def square():
    t.shape("square")
    t.right(90)

def triangle():
    t.shape("triangle")
    t.right(90)

def circle():
    t.shape("circle")
    t.right(90)

def stamp():
    t.stamp()


print("")
print("Welcome to Planet Drawer!")
print("")
print("STORY")
print("")
print("The International space station is trying to find diferrent planets.")
print("But, they are having trouble with remembering what the planets look like.")
print("You have to make pictures to show them what they are looking for!")
print("You can make any planet you want, just make sure its accurate!")
print("")
print("=====================================================================")
print("")
print("INSTRUCTIONS")
print("")
print("To draw: Click, then hold on the drawing circle. To change color: Press either R, O, Y, G, B, I, or V to change the color to the coresponding squares. To change background colors: Press either H, A, or P to change the color to the coresponding squares. To change shapes: Press either S, T, or C to change the color to the coresponding shapes. To change thickness: Press either 1, 2, 3, 4, 5, 6, or 7 to change the thickness to the coresponding circles. To add a shape: Press L to stamp the selected shape onto the canvas.")

ti = Turtle()
ti.penup()
ti.speed(0)

indent = -20
ti.goto(-200,80)
draw_symbol('Background:',5)

ti.goto(-200,30)
draw_square('black')
draw_symbol("H",-20)

ti.goto(-200,-20)
draw_square('gray')
draw_symbol("A",-20)

ti.goto(-200,-70)
draw_square('white')
draw_symbol("P",-20)

y = 180
indent = 42

ti.goto(-190,y)
draw_square('red')
draw_symbol("R", indent)

ti.goto(-130,y)
draw_square('orange')
draw_symbol("O", indent)

ti.goto(-70,y)
draw_square('yellow')
draw_symbol("Y", indent)

ti.goto(-10,y)
draw_square('green')
draw_symbol("G", indent)

ti.goto(50,y)
draw_square('blue')
draw_symbol("B", indent)

ti.goto(110,y)
draw_square('indigo')
draw_symbol("I", indent)

ti.goto(170,y)
draw_square('violet')
draw_symbol("V", indent)

x = 200
y = 150
indent = 30

ti.goto(x,140)
circle_t(5)
draw_symbol('1',indent)

ti.goto(x,100)
circle_t(7)
draw_symbol('2',indent)

ti.goto(x,60)
circle_t(9)
draw_symbol('3',indent)

ti.goto(x,20)
circle_t(11)
draw_symbol('4',indent)

ti.goto(x,-20)
circle_t(13)
draw_symbol('5',indent)

ti.goto(x,-55)
circle_t(15)
draw_symbol('6',indent)

ti.goto(x,-100)
circle_t(18)
draw_symbol('7',indent)

y = -150
indent = 42

ti.goto(-190,y)
draw_square('black')
draw_symbol("S", indent)

ti.goto(-130,y)
draw_triangle('black')
draw_symbol("T", indent)

ti.goto(-50,y)
ti.pendown()
ti.begin_fill()
ti.color('black')
ti.circle(20)
ti.end_fill()
ti.penup()
draw_symbol('C',indent)

t = Turtle()
t.color("blue")
t.width(5)
t.shape('circle')
t.pendown()
t.speed(3)

scr = t.getscreen()
scr.onscreenclick(move)

scr.onkey(red, "R")
scr.onkey(orange, "O")
scr.onkey(yellow, "Y")
scr.onkey(green, "G")
scr.onkey(blue, "B")
scr.onkey(indigo, "I")
scr.onkey(violet, "V")
scr.onkey(black, "H")
scr.onkey(white, "P")
scr.onkey(abu, "A")
scr.onkey(thickone, "1")
scr.onkey(thicktwo, "2")
scr.onkey(thickthree, "3")
scr.onkey(thickfour, "4")
scr.onkey(thickfive, "5")
scr.onkey(thicksix, "6")
scr.onkey(thickseven, "7")
scr.onkey(square, "S")
scr.onkey(triangle, "T")
scr.onkey(circle, "C")
scr.onkey(stamp, "L")
scr.onkey(red, "r")
scr.onkey(orange, "o")
scr.onkey(yellow, "y")
scr.onkey(green, "g")
scr.onkey(blue, "b")
scr.onkey(indigo, "i")
scr.onkey(violet, "v")
scr.onkey(black, "h")
scr.onkey(white, "p")
scr.onkey(abu, "a")
scr.onkey(thickone, "1")
scr.onkey(thicktwo, "2")
scr.onkey(thickthree, "3")
scr.onkey(thickfour, "4")
scr.onkey(thickfive, "5")
scr.onkey(thicksix, "6")
scr.onkey(thickseven, "7")
scr.onkey(square, "s")
scr.onkey(triangle, "t")
scr.onkey(circle, "c")
scr.onkey(stamp, "l")

scr.listen()
t.ondrag(draw)
