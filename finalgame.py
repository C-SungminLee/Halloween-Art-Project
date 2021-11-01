import turtle as trtl

import time
import random


t = trtl.Turtle()
rect = trtl.Turtle()
explosion = trtl.Turtle()


g = trtl.Turtle()
ufo = trtl.Turtle()
wn = trtl.Screen()
wn.addshape("explosion.gif")
explosion.hideturtle()
explosion.penup()
explosion.shape("explosion.gif")
explosion.goto(0,200)


wn.addshape("background.gif")
wn.bgpic("background.gif")
wn.addshape('ghost-flash.gif')
g.shape('ghost-flash.gif')
#wn.addshape('ufo.gif')
#ufo.shape('ufo.gif')
#wn.addshape('IMG_0933.gif')

rectCors = ((-5,20),(5,20),(5,-20),(-5,-20))

wn.register_shape('rectangle',rectCors)

rect.penup()
rect.turtlesize(2)
rect.goto(0,-275)
rect.color("orange")
rect.shape("square")
rect.stamp()


t.penup()
t.setheading(90)
t.goto(0,-250)
t.shape('rectangle')
t.color("orange")
ufo.speed(0)
ufo.penup()
ufo.goto(0, 200)
ufo.color("white")
wn.setup(600,600)
g.hideturtle()
g.penup()
g.goto(t.xcor(), t.ycor())
g.speed(0)

v = False








def left():
    if t.heading() <= 112.5:
        t.left(5.62500)

    else:
        print ("left")
def right():
    if t.heading() >= 67.5:
        t.right(5.62500)
    else:
        print ("right")
def attack():
    psotiontogo = random.randint(-200,200)
    global v
    if v == False:
        v = True
        g.penup()
        g.goto(t.xcor(), t.ycor())
        g.setheading(t.heading())
        g_a = g.clone()
        g_a.speed(0.51)
        g_a.showturtle()

        g_a.forward(475)
        time.sleep(0.00000001)
        print(str(g_a.xcor()) + ',' + str(g_a.ycor()))
        if int(ufo.xcor()-50)<g_a.xcor()<int(ufo.xcor()+50) and  200<g_a.ycor()<300:
            print('hit')
            g_a.hideturtle()
            explosion1 = explosion.clone()
            explosion1.goto(ufo.xcor(),ufo.ycor())
            explosion1.showturtle()
            time.sleep(0.1)
            explosion1.hideturtle()
            ufo.goto(psotiontogo,200)
            print('hiaaa')
        v = False


        g_a.hideturtle()





def left1():
  x = t.xcor()
  if -300<x<300: 
    t.setheading(180)
    t.forward(10)
    t.setheading(90)
def right1():
  x = t.xcor()
  if -300<x<300: 
    t.setheading(0)
    t.forward(10)
    t.setheading(90)






wn.onkey(left, "Left")
wn.onkey(right, "Right") 
wn.onkey(attack, "Up")
wn.onkey(left1, 'a')
wn.onkey(right1, 'd')

wn.listen()


wn.mainloop()



'''
while True:
  ufomove()
  time.sleep(1)
'''
# Snytax for keypress