import datetime
from time import time

def write(message):
    file = open("data.txt", "r")
    result = file.read().find(message)
    file.close()
    if result ==-1:
        time = datetime.datetime.now()
        file = open("data.txt","a")
        file.write(message +" ")
        file.write(str(time)+"\n")
        file.close
        