# Why Concurrency Creates Bugs

Single-threaded code has:

```text
One execution order
```

Concurrent code has:

```text
Many possible execution interleavings
```

That explosion creates:

* nondeterminism,
* timing dependence,
* hidden state corruption.

---

# Race Condition — Core Idea

A race condition means:

> Correctness depends on timing/order of execution.

This is the cleanest definition.

---

# Example

```python
counter = 0

def increment():
    global counter
    counter += 1
```

## Why This Is NOT Atomic

This line:

```python
counter += 1
```

is actually multiple operations:

```text
1. read counter
2. compute new value
3. write counter
```

Threads can interleave between these steps.

---

# 5. Dangerous Interleaving

Suppose:

```text
counter = 0
```

---

## Thread A

Reads:

```text
0
```

---

## Context switch

---

## Thread B

Reads:

```text
0
```

Adds 1:

```text
1
```

Writes:

```text
counter = 1
```

---

## Switch back to A

A still thinks counter was 0.

Adds 1:

```text
1
```

Writes:

```text
counter = 1
```

Final result:

```text
1
```

instead of:

```text
2
```

This is a race condition.

---

# Important Insight

The GIL does NOT prevent race conditions.

Huge misconception.

Why?

Because:

* the GIL switches between bytecode instructions,
* multi-step logical operations are still interruptible.

---

# Real Production Race Conditions

These are catastrophic.

Examples:

* double payments,
* inventory corruption,
* inconsistent cache state,
* lost updates,
* duplicate job execution,
* invalid financial balances.

---

# 8. How We Prevent Race Conditions

Using:

* locks,
* queues,
* immutability,
* actor models,
* transactional systems,
* atomic operations.

---

# 9. Python Lock

```python
import threading

lock = threading.Lock()
```

Usage:

```python
with lock:
    counter += 1
```

Now:

```text
Only one thread enters critical section at once.
```

---

# Critical Section

A critical section is:

> code accessing shared mutable state.

This concept appears everywhere in systems engineering.

---

# 11. Deadlock — Core Idea

Deadlock means:

> Two or more tasks wait forever on each other.

No progress possible.

---

# Deadlock Example

```python
lock_a = threading.Lock()
lock_b = threading.Lock()
```

---

## Thread 1

```python
with lock_a:
    with lock_b:
        ...
```

---

## Thread 2

```python
with lock_b:
    with lock_a:
        ...
```

---

# Deadlock Conditions

Deadlock requires:

| Condition        | Meaning                           |
| ---------------- | --------------------------------- |
| Mutual exclusion | resources locked                  |
| Hold and wait    | holding one while waiting another |
| No preemption    | cannot forcibly steal             |
| Circular wait    | cycle of dependencies             |

Break one → avoid deadlock.

---

# Production Prevention Strategy

Always acquire locks in:

> consistent global order.

Example:

```text
ALWAYS:
user lock
THEN
order lock
```

This is enormously important.

---

# Another Important Concurrency Bug — Livelock

Tasks keep reacting to each other:

* but no progress happens.

Like:

* two people repeatedly stepping aside in same direction.

Less common but real.

---

# Starvation

One thread/task never gets resources.

Example:

* unfair scheduling,
* lock monopolization.
