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
        self.k = keyboard
        self.recorded = ''
        self.alphabet = 'aabbccddeeffgghhiijjkkllmmnnooppqqrrssttuuvvwwxxyyzz'
    
    def record_keys(self):
        self.recorded = self.k.record(until='space', trigger_on_release=False)
    
    def start(self):
        print("\n\nPress space to begin writing the Alphabet\n\n")
        self.k.wait('space')
        print("\n\nWrite the Alphabet AS FAST AS YOU CAN!!! GO !!!\n\n!!! PRESS SPACE WHEN FINISHED !!!\n\n")
        self.timer = time.time()
        self.record_keys()
        

    def finish(self):
        print("Press SPACE for results!")
        self.k.wait('space')

        str0 = ''
        self.timer = (time.time() - self.timer)
         
        print("\nIt took you: ", self.timer, "s")
       
        for i in self.recorded:
            #(print(i.name+'\n'))
            str0 += i.name
        
        str1 = str0
        str1 = str1.replace('space', '')
        print("You entered: " + str1)
        print("Compared to: " + self.alphabet)

        if str1==self.alphabet:
            print("!!!!! ALL CORRECT !!!!! YOU WIN !!!!!")
            return False
        else:
            print("MISTAKES WERE MADE, TRY TRY AGAIN! PRESS SPACE TO TRY AGAIN")
            return True

user: str = input("Name : ")
t = Tangenta(user)

run = True

while run == True:
    t.start()
    run = t.finish()

# print("Starting Hook")
# keyboard.hook(t.capture_key)
# keyboard.wait('esc')
# print("Ending hook")
# print(t.finish())
# stop the count and get elapsed time
# print(time.time() - t0, "seconds wall time")

input("### THANK YOU CUM AGAIN ### Press enter to exit ###")
