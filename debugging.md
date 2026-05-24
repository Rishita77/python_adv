# Debugging Concurrent Systems 

Because bugs are:

* timing-dependent,
* nondeterministic,
* often unreproducible.

The worst kind of bugs.

---

# Why Logging Matters

Concurrency debugging heavily relies on:

```python
import logging
```

with:

* timestamps,
* thread IDs,
* task IDs,
* request IDs.

---

# Production Logging Pattern

Example format:

```text
timestamp | thread | request_id | action
```

This lets you reconstruct execution order.

---

# 22. Python Debugging Tools

---

## `pdb`

Built-in debugger.

```python
import pdb; pdb.set_trace()
```

Lets you:

* inspect state,
* step execution,
* examine stack frames.

---

## `faulthandler`

Useful for deadlocks/hangs.

```python
import faulthandler
faulthandler.dump_traceback_later(10)
```

Can dump stuck thread stacks.

---

# Inspecting Running Threads

```python
threading.enumerate()
```

shows active threads.

Useful during hangs.

---

# Profiling — Core Idea

Profiling answers:

> Where is time actually spent?

This is crucial to understand performance bottlenecks.


## CPU Profiling

Measures:

* function execution time,
* call counts,
* hotspots.


## cProfile

```python
import cProfile

cProfile.run("my_function()")
```

Shows:

* cumulative time,
* per-call time,
* function hierarchy.

## Important Profiling Point

Usually:

> 90% of runtime is in 10% of code.

Optimization without profiling is dangerous.


### I/O Profiling

CPU profilers miss:

* waiting,
* DB latency,
* network delays.


# Race Conditions in Asyncio


Async code can ALSO have race conditions.

Example:

```python
shared = []

async def worker():
    shared.append(1)
```

If operations interleave badly:

* corruption/inconsistency possible.

Async avoids SOME threading problems:

* but not shared-state problems.

---

# Most Important Production Principle

The safest concurrent systems minimize:

> shared mutable state.

This is one of the deepest truths in systems design.

Why modern systems favor:

* queues,
* message passing,
* immutable data,
* actors,
* event streams.

Because locks become extremely hard at scale.

Examples:

* Redis queues,
* Kafka,
* actor systems,
* multiprocessing workers,
* async message passing.