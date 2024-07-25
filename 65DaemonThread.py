# 65. Daemon Thread [05:53:35]----------------------------------------------------------------------
# Daemon Thread = a thread that run in the background, not important for program to run 
# your program will not wait for daemon threads to complete before exiting
# non-daemon threads cannot normallly be killed, stay alive until task is complete
# ex: background tasks, garbage collection, wainting for input long running process

import threading
import time
def timer():
    print()
    print()
    count = 0
    while True: 
        time.sleep(1)
        count+=1
        print()
        print("Logged in for: ", count, "seconds")

x=threading.Thread(target=timer)
x.setDaemon(True)

x.start()
print(x.daemon)
answer=input("Do you wish to exit?: ")
print(answer)
# ,args=(),daemon=True