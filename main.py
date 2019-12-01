"""
Create the game "TypeME"
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

# sys.path.append('..')

def mainMenu():
    os.system('cls')
    print("###################################")
    print("#                                 #")
    print("#        Welcome to TypeME        #")
    print("#                                 #")
    print("#        1. to start game         #")
    print("#        2. to view highscore     #")
    print("#        3. to quit               #")
    print("#                                 #")
    print("###################################")

    ui = input("Please enter choice: ")

    if ui == '1':
        t.start()
        return t.finish()
    elif ui == '2':
        highScore()
    elif ui == '3':
        return False

def highScore():
    players = {}

    # parse first file
    with open("highscore.txt") as raw_file:
        reader = csv.reader(raw_file, delimiter=":")
        
        for rows in reader:
            print(rows)

        input("Press Enter to continue")
        mainMenu()

""""
        for row in reader:
            value = row[1]
            name = row[0]
            players[name] = value
    
    # filter second file and write output to third
    base_file = open('highscore.txt', 'r')
    base_file2 = base_file

    reader = csv.reader(base_file, delimiter=":")
    # writer = csv.writer(filtered_file, delimiter=":")

    # copy headers
    headers = next(reader)
    writer.writerow(headers)

    for row in reader:
        name = row[0]

        if name in companies:
            row[0] = companies[name]
            writer.writerow(row)
    
    #    elif name not in companies: 
    #        writer.writerow(row)

    base_file.close()
    #filtered_file.close()
"""


class Tangenta:
    def __init__(self, player):
        self.player = player
        self.timer = 0
        self.score = 0
        self.k = keyboard
        self.recorded = ''
        self.alphabet = 'abcdefghijklmnopqrstuvwxyz'

    def record_keys(self):
        self.recorded = self.k.record(until='enter', trigger_on_release=False)
    
    def start(self):
        print("\n\nPress space to begin writing the Alphabet\n\n")
        self.k.wait('space')
        print("\n\n!!! Write the Alphabet AS FAST AS YOU CAN !!! GO !!!\n\n!!! PRESS ENTER WHEN FINISHED !!!\n\n")
        self.timer = time.time()
        self.record_keys()
        input(":")

    def finish(self):
        print("Press ENTER for results!")
        self.k.wait('enter')

        str0 = ''
        self.timer = (time.time() - self.timer)
        self.score = self.timer
         
        print("\nIt took you: ", self.timer, "s")
       
        for i in self.recorded:
            str0 += i.name
        
        str1 = str0
        str1 = str1.replace('space', '')
        str1 = str1.replace('enter', '')
        str1 = str1[::2]
        print("You entered: " + str1)
        print("Compared to: " + self.alphabet)

        if str1==self.alphabet:
            print("!!!!! ALL CORRECT !!!!! YOU WIN !!!!!")
            print("!!! Printing Highscore !!!")
            print(self.player + " : " + str(self.score))

            with open('highscore.txt', 'a') as f:
                f.write("\n" + self.player + ":" + str(self.score))
            
            play_again = False
            input("#:")
            answer = input("Play again? yes/no:")
            
            if answer == 'yes':
                return True
            else:
                return False
        else:
            print("MISTAKES WERE MADE, TRY TRY AGAIN! PRESS SPACE TO TRY AGAIN")
            input(" ")
            input("Press Enter to Continue")
            return True

user: str = input("Name : ")
t = Tangenta(user)

run = True

while run == True:
    run = mainMenu()

input("### THANK YOU CUM AGAIN ### Press enter to exit ###")