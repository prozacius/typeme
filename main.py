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
import time, os, math, keyboard, string, sys
sys.path.append('..')

class Tangenta:
    pass

#def print_pressed_keys(e):
#    line = ', '.join(str(code) for code in keyboard._pressed_events)
	# '\r' and end='' overwrites the previous line.
	# ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
#    print('\r' + line + ' '*40, end='')

def print_pressed_keys(e):
    line = ', '.join(str(code) for code in keyboard._pressed_events)
	# '\r' and end='' overwrites the previous line.
	# ' '*40 prints 40 spaces at the end to ensure the previous line is cleared.
    print('\r' + line + ' '*40, end='')
g

keys = list(string.ascii_lowercase)

print(keys)
print("Starting Hook")
keyboard.hook(print_pressed_keys)
keyboard.wait('esc')
print("Ending hook")
input("Press enter to exit")