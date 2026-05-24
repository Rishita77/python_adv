# Event Loop
An event loop is fundamentally just:

A scheduler for cooperative tasks

Its entire job is:

- decide what task runs next
- pause tasks that are waiting
- resume tasks when events complete

## The Event Loop Core Algorithm

At a high level:

while True:
    
- check completed I/O events
- wake waiting tasks 
- run scheduled callbacks 
- execute ready coroutines 
- pause coroutines at await points


This repeats thousands of times per second.

### The Ready Queue

The event loop maintains something like:

READY TASKS:
- task A
- task B
- task C

It picks one:

`run task A`

until
task finishes,
OR task hits await.


## What Is a Coroutine REALLY?

When Python sees:

`async def fetch():`
    
It does NOT immediately run the function. Instead, it creates a:
**coroutine function.**

Calling it:
`coro = fetch()`

does NOT execute it.

It creates a coroutine object.

Think of it as : A paused computation

similar to: generators, resumable functions,
suspended stack frames.

### Coroutine Object Mental Model

Think of this:

`async def work():`

    print("A")
    await asyncio.sleep(1)
    print("B")`

as becoming internally something like:

Coroutine Object:

{
*     current_instruction,
*     local_variables,
*     execution_state,
*     awaiting_on,
*     completion_status
}

It is basically:

a suspended computation.

### Who Executes the Coroutine?

The event loop.

Example:

`asyncio.run(hello())`