# 64. Multithreading[05:40:00]------------------------------------------------------------
import threading
import time
def eat_breakfast():
    time.sleep(3)
    print("You ate breakfast")
def drink_coffee():
    time.sleep(4)
    print("You drank coffee")
def study():
    time.sleep(5)
    print("You studied")
x=threading.Thread(target=eat_breakfast,args=())
x.start()
y=threading.Thread(target=drink_coffee,args=())
y.start()
z=threading.Thread(target=study,args=())
z.start()


# Now joining multiple threads with the main thread
x.join()
y.join()
z.join()


# eat_breakfast()
# drink_coffee()
# study()


print(threading.active_count())
print(threading.enumerate())
print(time.perf_counter())