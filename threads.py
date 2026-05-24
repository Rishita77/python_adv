import threading
import time


def work(name):
    print(f"{name} starting")
    time.sleep(2)
    print(f"{name} done")


t1 = threading.Thread(target=work("A"))
t2 = threading.Thread(target=work("B"))

t1.start()
t2.start()

t1.join()
t2.join()


# Due to GIL only one of the threads is getting executed and ultimately running one by one. Then What's the point of
# threads? So threads are still used in python because most real-world programs spend huge amounts of time NOT
# executing Python bytecode.
# Moreover, when one thread waits on I/O calls, the GIL is released and hence the other threads can execute.
# So, threads are not good for CPU-heavy Python code.
