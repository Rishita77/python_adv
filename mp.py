from multiprocessing import Process
import time


def cpu_heavy():
    total = 0
    for i in range(100_000_000):
        total += i


p1 = Process(target=cpu_heavy)
p2 = Process(target=cpu_heavy)

start = time.time()

p2.start()

p1.join()
p2.join()

print("Done:", time.time() - start)

# Each process:
#
# has its own Python interpreter,
# own memory,
# own GIL.
#
# Now true parallelism happens.
# p1.start()

# But Processes Are Expensive as compared to threads:
#
# more memory,
# IPC overhead,
# serialization cost.
#
# So don't use them for lightweight I/O.
