import threading
import time

def task1():
    print("Task 1: Downloading file")
    time.sleep(1)
    print("Task 1 completed")

def task2():
    print("Task 2: Processing data")
    time.sleep(1)
    print("Task 2 completed")

def task3():
    print("Task 3: Sending email")
    time.sleep(1)
    print("Task 3 completed")

t1 = threading.Thread(target=task1)
t2 = threading.Thread(target=task2)
t3 = threading.Thread(target=task3)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All tasks completed")
