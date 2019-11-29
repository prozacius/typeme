"""
11. Create the game "TypeME"
Create a class called "Tangenta". Use the time library to keep track of time.
When the object has been created the program should ask if you want to play Tangenta.

By pressing space the stopwatch start and you're supposed to write the alphabet (A-Z) as fast as
possible. Use the library keyboard. When you are done you press space again to stop the time

Compare what was written to the alphabet in order. If it is correct the program should ask the user
for a name and save name and time to a textfile.

If not it should ask if the user wants to play again.

Bonus: Count how many mistakes or if some characters have been missed. Penalty is 1 sec per mistake/missing letter.
"""
import time, os, math, keyboard, string, sys, csv, threading

sys.path.append('..')


class Tangenta:
    def __init__(self, player):
        self.player = player
        self.timer = 0
        self.score = 0

    def start(self):
        self.timer = time.time()

    def finish(self):
        self.timer = (time.time() - self.timer)
        return self.timer


def capture_key(k):
    print(k.name)
    return k.name


# t0 = time.time()

t = Tangenta(input("Player Name: "))

print("Starting Hook")
keyboard.hook(capture_key)
keyboard.wait('esc')
print("Ending hook")
print(t.finish())
# stop the count and get elapsed time
# print(time.time() - t0, "seconds wall time")
input("Press enter to exit")
