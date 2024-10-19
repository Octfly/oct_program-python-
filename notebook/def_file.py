import pickle
import sys
i = ""
u = "kong"
xin = "kong"

def load():
    global i
    with open('jishi_save_data.pkl','rb') as f:
        loaded = pickle.load(f)
        i = (loaded[0])
        print(i)
def save():
    global u,i
    re = str(input("请输入选择(plus or reset)："))
    if re == "plus":
        with open('jishi_save_data.pkl','rb') as f:
            loaded = pickle.load(f)
            i = (loaded[0])
        i = str(i) + str(u)
        data = [i]
        with open('jishi_save_data.pkl','wb') as f:
            pickle.dump(data,f)
        print("保存成功")

    if re == "reset":
        i = ""
        i = str(i) + str(u)
        data = [i]
        with open('jishi_save_data.pkl','wb') as f:
            pickle.dump(data,f)
        print("保存成功")

def u2():
    global u
    u = str(input("请输入文本(读取or写入or quit)："))