import time
sjc = time.time()
i = 0
while i < 450000000:
    i += 1
n = time.time()
z = n - sjc
print("运行时间：")
print(z)

print("CPU分数：")
zn = (round(z,4))*10000
print(1000000 - zn*3)