import random

def faf():
    de = ''.join([str(random.randint(0,9)) for x in range(7)])
    print(de)

faf()