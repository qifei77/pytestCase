import time
import random
import string

#时间戳
def timestamp():
    return int(time.time())
#随机字符串
def random_str(length=8):
    return ''.join(random.choices(string.ascii_lowercase, k=length))
#随机整数

def random_int(start=1000,end = 9999):
    return str(random.randint(start,end))

