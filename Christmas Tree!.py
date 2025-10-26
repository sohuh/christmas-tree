import time 
import os 
import sys 
import random

# Define the terminal colors
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
RESET = "\033[0m"


# Christmas Tree's 

TREE = [
    "         *         ",
    "        ***        ",
    "       *****       ",
    "      *******      ",
    "     *********     ",
    "    ***********    ",
    "        |||        "
]

SONG = [
    "Last Christmas, I gave you my heart",
    "But the very next day, you gave it away",
    "This year, to save me from tears",
    "I'll give it to someone special",
    "Last Christmas, I gave you my heart",
    "But the very next day, you gave it away",
    "This year, to save me from tears",
    "I'll give it to someone special",
    "Once bitten and twice shy",
    "I keep my distance, but you still catch my eye",
    "Tell me, baby, do you recognize me?",
    "Well, it's been a year, it doesn't surprisе me",
    "'Happy Christmas', I wrapped it up and sent it",
    "With a notе saying 'I love you', I meant it",
    "Now I know what a fool I've been",
    "But if you kissed me now, I know you'd fool me again"
]

def glowing_tree():
    os.system('cls' if os.name =='nt' else 'clear')
    for row in TREE:
       print(row)
       #new_row = ""
        #for ch in row:
            #if ch == "*":
                #new_row += random.choice([RED,GREEN,YELLOW]) + "*" + RESET
            #else:
                #new_row += ch
            #print(new_row)
def slow_typing(test, delay =0.05):
    for char in test:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    for i in range(3):
        glowing_tree()
        time.sleep(0.6)
        os.system('cls' if os.name == 'nt' else 'clear')
    
    print("\n")
    time.sleep(0.5)
    for line in SONG:
        print(" " * 25, end="")
        slow_typing(line)
        time.sleep(0.8)

if __name__ == "__main__":
    main()