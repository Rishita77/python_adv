# When to use what:

| Work Type              | Best Tool       |
|------------------------|-----------------|
| High-scale networking  | Asyncio         |
| Blocking I/O libraries | Threads         |
| CPU-heavy tasks        | Multiprocessing |
| Mixed systems          | Combination     |


# Example usage/architecture:

```Text
Async API server
    ↓
Thread pool for blocking DB drivers
    ↓
Process pool for CPU-heavy tasks
```


# Threads
```
Thread A ----wait----
Thread B ----wait----
(OS switches)
```

# Async
```
Task A --await-->
                Task B --await-->
                               Task C
```

One thread.
Cooperative switching.