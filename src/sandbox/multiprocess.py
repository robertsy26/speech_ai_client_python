import multiprocessing as mp

import threading

def task1():
    sum = 0
    for num in range(1,11):
        sum += num
    print(sum)

def task2():
    product = 1
    for num in range(1,11):
        product *= num
    print(product)

def task3():
    sum = 0
    for num in range(1,11):
        sum -= num
    print(sum)

if __name__ == "__main__":
    process1 = mp.Process(target=task1)
    process1.start()
    print(f'Process created: {process1.name}')

    process2 = mp.Process(target=task2)
    process2.start()
    print(f'Thread created: {process2.name}')

    process3 = mp.Process(target=task3)
    process3.start()
    print(f'Thread created: {process3.name}')

    process1.join()
    process2.join()
    process3.join()

'''
# Queue
queue = []
print(queue)

for num in range(1,11): 
    if (len(queue) >= 3):
        queue.pop(0)
    queue.append(num)
    print(queue)

for num in range(10):
    print(num)
'''