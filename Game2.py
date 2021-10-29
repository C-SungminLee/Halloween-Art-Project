import random
import turtle as trtl
import time
wn = trtl.Screen()
wn.screensize(400,400)


t = trtl.Turtle()

ufo = trtl.Turtle()

blu = trtl.Turtle()


ghost = trtl.Turtle()

ghost.speed(1)


wn.addshape('IMG_0933.gif')
wn.addshape('ghost-flash.gif')
blu.penup()
blu.goto(0,-250)
blu.shape('IMG_0933.gif')

ghost.penup()
ghost.hideturtle()
ghost.shape('ghost-flash.gif')
ghost.goto(blu.xcor(),blu.ycor())


def left():
  x = blu.xcor()
  if -300<x<300: 
    blu.setheading(180)
    blu.forward(10)
def right():
  x = blu.xcor()
  if -300<x<300: 
    blu.setheading(0)
    blu.forward(10)
def attack():
  ghost.clone()
  ghost.hideturtle()
  ghost.setheading(90) 
  ghost.showturtle() 
  ghost.forward(500)


def space():
  attack()


  
'''
# Temporary 
ufo.penup()
ufo.goto(0, 300)


def ufomove():
  ufo.speed(5)
  lengthtomove = random.randint(-100,100)
  ufo.goto(+lengthtomove,250)

while True:
  ufomove()
  time.sleep(1)
'''
# Snytax for keypress

wn.onkeypress(left, 'Left')
wn.onkeypress(right, 'Right')
wn.onkeypress(space, 'Up')
wn.listen()




wn.mainloop() 