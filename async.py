# Async is NOT:
# threads, parallelism or background execution.
#
# This is: cooperative concurrency.

# Core Async Principle
#
# Instead of: OS decides when threads switch
# We do: Tasks voluntarily pause themselves

# Asyncio uses:
#
# ONE thread,
# ONE event loop,
# MANY tasks.
#
# The event loop repeatedly does:
#
# while True:
#     check ready tasks
#     run one
#     pause when awaiting
#     switch to another


import asyncio


async def task(name):
    print(f"{name} started")
    await asyncio.sleep(2)
    print(f"{name} done")


async def main():
    await asyncio.gather(
        task("A"),
        task("B")
    )


asyncio.run(main())

# What await REALLY Means
# "I cannot make progress now. Let another task run."


# Why Async Scales Better Than Threads?
#
# Threads have overhead:
# stacks,
# kernel scheduling,
# context switching,
# memory.
#
# 10k threads is bad.
#
# But async tasks are lightweight.
# 10k async connections is normal.
#
# That's why: FastAPI, Node.js, Nginx, high-scale APIs use event-loop models.

# But even async with no yield CPU work fails

