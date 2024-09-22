i = 0
import time
sjc = time.time()
while i < 10000:
    print(i)
    i += 1
    n = time.time()
print("CPU分数：")
z = n - sjc
zn = ((round(z,5))*10000)
print(round(10000 - zn))
time.sleep(5)