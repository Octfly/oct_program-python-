import turtle as t
import random
import time
import sys
sjc = time.time()
kssjc = 0
sczimu = 0
z = 0

 #########################
game = t.Screen()
game.title("fanyinli")
game.bgcolor("yellow")
game.setup(800,600)
game.tracer(0)

pen = t.Turtle()
pen.ht()
pen.up()
pen.color('white')
pen.goto(0,0)

pen2 = t.Turtle()
pen2.ht()
pen2.up()
pen2.color('white')
pen2.goto(60,0)

pen3 = t.Turtle()
pen3.ht()
pen3.up()
pen3.color('white')
pen3.goto(0,60)

time.sleep(random.randint(1,5))
game.bgcolor("lightblue")
kssjc = time.time()
pen2.write("毫秒",align="center",font=("Arial",20,'bold'))

def ting():
    global z,n
    time.sleep(3)
    z += 1

game.listen()
game.onkey(ting,' ')

while True:
    if sczimu >= 400:
        n = "多练练，低于平均水平"
    elif sczimu >= 300 and sczimu <= 399:
        n = "正常水平"
    elif sczimu >= 250 and sczimu <= 299:
        n = "牛"
    elif sczimu >= 200 and sczimu <= 249:
        n = "普通人中的顶尖"
    elif sczimu >= 100 and sczimu <= 199:
        n = "你已经达到职业运动员的水准"
    elif sczimu <= 100:
        n = "我知道，你是预判"  
    game.update()
    sjc = time.time()
    sczimu = (sjc - kssjc) * 1000
    pen.clear()
    pen3.clear()
    print(z)
    pen3.write(n,align="center",font=("Arial",20,'bold'))
    pen.write(round(sczimu),align="center",font=("Arial",20,'bold'))
    if z == 1:
        False()
