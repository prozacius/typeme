"""
11. Skapa spelet Tangenta!
Klassen ska heta Tangenta. Använd biblioteket time för att hålla reda på tiden.
När objektet har skapats ska programmet fråga om man vill spela Tangenta.

Om man klickar mellanslag ska stoppuret sättas igång och man ska skriva in alfabetet (A-Z) så fort som
möjligt. Använd biblioteket keyboard. När man är klar ska man klicka mellanslag igen för att
stoppa tiden.

Man jämför sedan att det man skrivit in är alfabetet i ordning. Om det stämmer
ska programmet fråga användaren om ett namn och spara namn samt tiden i en textfil.
Om inte ska den fråga om man vill spela igen.

Bonus: Räkna hur många fel man skrivit eller om man missat några bokstäver. Strafftid är 1
sekund per fel/saknad bokstav.
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
