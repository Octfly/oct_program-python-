import turtle as t
import random     
import pickle      #导入类库
#创建窗口



game = t.Screen()
game.title("jishu")
game.bgcolor('orange')
game.setup(400,400)
game.tracer(0)






#色块
p2 = t.Turtle()
p2.ht()#隐藏
p2.up()
p2.speed(0)
p2.color('white')
p2.shape('square')
p2.shapesize(1,2)
p2.goto(-170,180)
p2.st()#显示

p3 = t.Turtle()
p3.ht()#隐藏
p3.up()
p3.speed(0)
p3.color('blue')
p3.shape('square')
p3.shapesize(1,2)
p3.goto(-95,180)
p3.st()#显示

p4 = t.Turtle()
p4.ht()#隐藏
p4.up()
p4.speed(0)
p4.color('purple')
p4.shape('square')
p4.shapesize(1,2)
p4.goto(-20,180)
p4.st()#显示

p5 = t.Turtle()
p5.ht()#隐藏
p5.up()
p5.speed(0)
p5.color('yellow')
p5.shape('square')
p5.shapesize(1,2)
p5.goto(55,180)
p5.st()#显示

p6 = t.Turtle()
p6.ht()#隐藏
p6.up()
p6.speed(0)
p6.color('red')
p6.shape('circle')
p6.shapesize(2,2)
p6.goto(-170,-160)
p6.st()#显示

p7 = t.Turtle()
p7.ht()#隐藏
p7.up()
p7.speed(0)
p7.color('pink')
p7.shape('circle')
p7.shapesize(2,2)
p7.goto(-90,-160)
p7.st()#显示

q6 = 0
w6 = 0
q5 = 0
w5 = 0
q4 = 0
w4 = 0
q3 = 0
w3 = 0
q2 = 0
w2 = 0
q = 0
w = 0
i = 0



def load():
    global i,w,q,q2,w2,q3,w3,q4,w4,q5,w5,q6,w6
    with open('save_data.pkl','rb') as f:
        loaded = pickle.load(f)
        print(loaded)


        q6 = 0
        w6 = (loaded[6])
        q5 = 0
        w5 = (loaded[5])
        q4 = 0
        w4 = (loaded[4])
        q3 = 0
        w3 = (loaded[3])
        q2 = 0
        w2 = (loaded[2])
        q = 0
        w = (loaded[1])
        i = (loaded[0])

def p():
    data = [i,w,w2,w3,w4,w5,w6]
    with open('save_data.pkl','wb') as f:
        pickle.dump(data,f)

#色块数字与“笔”
#白
pen2 = t.Turtle()
pen2.ht()
pen2.up()
pen2.color('black')
pen2.goto(-130,160)



#蓝
pen3 = t.Turtle()
pen3.ht()
pen3.up()
pen3.color('black')
pen3.goto(-55,160)


#紫
pen4 = t.Turtle()
pen4.ht()
pen4.up()
pen4.color('black')
pen4.goto(20,160)


#金
pen5 = t.Turtle()
pen5.ht()
pen5.up()
pen5.color('black')
pen5.goto(95,160)




pen6 = t.Turtle()
pen6.ht()
pen6.up()
pen6.color('black')
pen6.goto(-130,-180)



pen7 = t.Turtle()
pen7.ht()
pen7.up()
pen7.color('black')
pen7.goto(-50,-180)



#def用法

def text():
    global i,q,w,q2,w2,q3,w3,q4,w4,q5,w5,q6,w6#global声明
    i += 1
    c = "{}".format(i)
    pen.clear()
    pen.write(c,align="center",font=("Arial",20,'bold'))#变化计数
#白色掉落物
    if(i + 1):
        q += 1
    if(q/(random.randint(70,120))) > 1:
        w += 1
        q = 0

    pen2.clear()
    pen2.write(w,align="center",font=("Arial",20,'bold'))
#蓝色掉落物
    if(i + 1):
        q2 += 1
    if(q2/(random.randint(800,1200))) > 1:
        w2 += 1
        q2 = 0

    pen3.clear()
    pen3.write(w2,align="center",font=("Arial",20,'bold'))
#紫色掉落物
    if(i + 1):
        q3 += 1
    if(q3/(random.randint(9000,12000))) > 1:
        w3 += 1
        q3 = 0

    pen4.clear()
    pen4.write(w3,align="center",font=("Arial",20,'bold'))

#金色掉落物
    if(i + 1):
        q4 += 1
    if(q4/(random.randint(100000,120000))) > 1:
        w4 += 1
        q4 = 0

    pen5.clear()
    pen5.write(w4,align="center",font=("Arial",20,'bold'))
#圆1
    if(i + 1):
        q5 += 1
    if(q5/(random.randint(10,20))) > 1:
        w5 += 1
        q5 = 0

    pen6.clear()
    pen6.write(w5,align="center",font=("Arial",20,'bold'))
#圆2
    if(i + 1):
        q6 += 1
    if(q6/(random.randint(60,70))) > 1:
        w6 += 1
        q6 = 0

    pen7.clear()
    pen7.write(w6,align="center",font=("Arial",20,'bold'))



#监听键盘
game.listen()
game.onkey(text,' ')
game.onkey(load,'Tab')
game.onkey(p,'p')
#计数显示
pen = t.Turtle()
pen.ht()
pen.up()
pen.color('red')
pen.goto(0,0)
c = "{}".format(i)
pen.write(c,align="center",font=("Arial",20,'bold'))


while True:
    game.update()#刷新
    
        
    
