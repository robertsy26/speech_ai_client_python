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

thread1 = threading.Thread(target=task1)
thread1.start()
print(f'Thread created: {thread1.name}')

thread2 = threading.Thread(target=task2)
thread2.start()
print(f'Thread created: {thread2.name}')

thread3 = threading.Thread(target=task3)
thread3.start()
print(f'Thread created: {thread3.name}')

thread1.join()
thread2.join()
thread3.join()

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