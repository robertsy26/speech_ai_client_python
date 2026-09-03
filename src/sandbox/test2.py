import time
import queue
import random

to_run = queue.Queue()

def enter():
    num = random.randint(1,10)

if __name__ == "__main__":
    while True:
        if to_run.qsize() > 0:
            print(to_run.get())
        else:  
            print("Empty")
        time.sleep(5)