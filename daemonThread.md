# Daemon vs Non-Daemon threads

## What Keeps a Process Running?

A Python program is ultimately:

* one OS process,
* containing threads.

The process exits when:

> the interpreter decides there is no more important work left.

Python distinguishes between:

* daemon threads,
* non-daemon threads.

because it needs to know:

```text
Should this thread prevent process shutdown?
```

That’s the actual purpose.

---

# 2. Non-Daemon Threads (Default)

By default:

```python
import threading

t = threading.Thread(target=work)
```

creates:

> a non-daemon thread.

Meaning:

```text
"This thread is important.
Do NOT terminate the process until it finishes."
```

---

# 3. Example

```python
import threading
import time

def worker():
    print("Worker started")
    time.sleep(5)
    print("Worker finished")

t = threading.Thread(target=worker)

t.start()

print("Main thread finished")
```

Output:

```text
Main thread finished
(waits 5 seconds)
Worker finished
```

Why?

Because:

* the worker thread is non-daemon,
* Python waits for it before exiting.

---

# 4. Daemon Threads

Now:

```python
t.daemon = True
```

means:

```text
"This thread is background/supporting work.
If the process exits, abandon it."
```

---

# 5. Example

```python
import threading
import time

def worker():
    while True:
        print("Working...")
        time.sleep(1)

t = threading.Thread(target=worker)
t.daemon = True

t.start()

print("Main thread exiting")
```

Output:

```text
Working...
Main thread exiting
(program exits immediately)
```

The daemon thread is killed abruptly.

---

# 6. The Important Runtime Rule

Python exits when:

```text
NO non-daemon threads remain alive
```

This is the actual rule.

---

# 7. The Main Thread

The initial Python thread is:

> the main thread.

It is always non-daemon.

When it finishes:

* Python checks remaining threads.

If only daemon threads remain:

* interpreter exits.

---

# 8. Why Daemon Threads Exist

Daemon threads are for:

* background monitoring,
* metrics collection,
* periodic cleanup,
* cache refreshers,
* heartbeat systems,
* logging flushers,
* internal support services.

Things that should NOT block shutdown.

---

# 9. Why Abrupt Shutdown Is Dangerous

Daemon threads are NOT gracefully cleaned up.

They can be terminated:

* mid-function,
* mid-write,
* while holding locks,
* while writing files,
* while updating DB state.

This is extremely important.

---

# 10. Example of Dangerous Daemon Behavior

```python
def save_data():
    with open("data.txt", "w") as f:
        f.write("important data")
        time.sleep(10)
```

If daemon thread dies midway:

```text
corrupted/incomplete write
```

Possible.

Because Python does NOT wait for daemon completion.

---

# 11. Production Rule

Use daemon threads only for:

* expendable background work.

Never for:

* critical persistence,
* financial transactions,
* DB consistency,
* essential cleanup.

---

# 12. Why “Daemon” Name Exists

Historically from Unix:

> daemons = background service processes.

Python borrowed the term for:

> background service threads.

But:

* Python daemon threads are NOT OS daemons.

Different concept.

---

# Important Difference From Async Tasks

Async tasks:

* can support structured cancellation,
* cleanup with `finally`,
* controlled shutdown.

Daemon threads:

* are much cruder,
* closer to “fire-and-forget.”

---

# Tiny Visual Model

## Non-daemon

```text
Main thread done
↓
Wait for worker
↓
Exit
```

---

## Daemon

```text
Main thread done
↓
Kill remaining daemon threads
↓
Exit immediately
```

---

# Inheritance Rule

Threads inherit daemon status from parent thread.

Usually:

* main thread = non-daemon,
* child threads default to non-daemon.

But daemon threads create daemon children by default.

---

# Important Production Shutdown Pattern

Good production systems avoid daemon reliance.

Instead:

```text
1. signal shutdown
2. stop accepting work
3. gracefully drain tasks
4. join worker threads
5. clean exit
```