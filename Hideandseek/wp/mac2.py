import uuid
import random

mac = "02:42:ac:12:00:02"
temp = mac.split(':')
temp = [int(i,16) for i in temp]
temp = [bin(i).replace('0b','').zfill(8) for i in temp]
temp = ''.join(temp)
mac = int(temp,2)
random.seed(mac)
randStr = str(random.random()*100)
print(randStr)
# 2.974954236670335
#结果为 97.9970136622037