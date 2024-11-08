import turtle as t
import def_F

#监听键盘
def_F.game.listen()
def_F.game.onkey(def_F.text,' ')
def_F.game.onkey(def_F.load,'Tab')
def_F.game.onkey(def_F.p,'p')
def_F.game.onkey(def_F.cc1,'1')
def_F.game.onkey(def_F.cc2,'2')
def_F.game.onkey(def_F.cc3,'3')
def_F.game.onkey(def_F.cc4,'4')

while True:
    def_F.game.update()#刷新