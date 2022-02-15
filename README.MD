# Credits/Info

Developer: Ghoul @NotGhoull
Dependances: Typing, time, winsound, os
Python Version: 3.9.5
Note: Please send feedback for things that I should change/add

---

## Installation

`pip install package`

---

## Code example

### How to import the library

(classes.countdown may be diffrent for you this is the location of the script!)

```python
from classes.countdown import CountdownHandler
```

### Start a countdown

```python
from classes.countdown import CountdownHandler

countdown = CountdownHandler(10)
countdown.start()
```

This will start a countdown for 10 seconds

### Add a sound effect

```python
from classes.countdown import CountdownHandler

countdown = CountdownHandler(10, True)
countdown.start()
```

The True inside of the CountdownHandler function says to enable "sfx mode" you can then supply the location of the sound effect "/sounds/mycoolsfx.wav"

---

## Functions

### Init

> Args: time: [Float, Int] (REQUIRED) | playSound [Bool] (OPTIONAL) | soundLoc [str] (OPTIONAL)
> Description: Initializeation function
> Usage: countdown = CountdownHandler(ARGS)

### start

> Description: Starts the countdown timer using self.time
> usage: CountdownHandler.start()

---

## Variable

> self.time
> self.is_running: Bool
> self.playSound: Bool
> self.soundLoc: str

### How to access Variables

To access the variables just use the name of the variable you want and type it in (Best used in if statement with threading)

EXAMPLE:

```python
from classes.countdown import CountdownHandler
count = CountdownHandler(10)

if count.is_running == False:
    print("The countdown isn't running!")
```

---

## ToDo

- [ ] Turn into a installable python package
