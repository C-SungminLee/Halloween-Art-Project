import random
import turtle as trtl
import time
wn = trtl.Screen()
wn.screensize(400,400)


t = trtl.Turtle()

ufo = trtl.Turtle()

blu = trtl.Turtle()

wn.addshape('IMG_0933.gif')
blu.penup()
blu.goto(0,-250)
blu.shape('IMG_0933.gif')

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

# Temporary 
ufo.penup()
ufo.goto(0, 300)


def ufomove():
  ufo.speed(5)
  lengthtomove = random.randint(-100,100)
  ufo.goto(0+lengthtomove,300)

while True:
  ufomove()
  time.sleep(1)
# Snytax for keypress

wn.onkeypress(left, 'Left')
wn.onkeypress(right, 'Right')
wn.listen()




wn.mainloop()