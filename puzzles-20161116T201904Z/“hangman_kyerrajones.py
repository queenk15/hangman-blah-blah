#Kyerra Jones
#
#
#10/19/16

import os
import random

def show_start_screen():
    print("Let's play Hangman!")
    print("   \\  //       \\\  ///   \/   \\\    ///       \\\  ///") 
    print("   (o)(o)   /)  ((O)(O))  (OO)  ((O)  (O))   /)  ((O)(O)) ")
    print("   ||  || (o)(O) | \ || ,'.--.)  | \  / |  (o)(O) | \ ||  ")
    print("   |(__)|  //\\  ||\\||/ /|_|_\  ||\\//||   //\\  ||\\||  ")
    print("   /.--.\ |(__)| || \ || \_.--.  || \/ ||  |(__)| || \ |  ")
    print("  -'    `-/,-. | ||  ||'.   \) \ ||    ||  /,-. | ||  ||  ")
    print("         -'   ''(_/  \_) `-.(_.'(_/    \_)-'   ''(_/  \_) ")

    
    

def show_end_screen():
    print("Goodbye")
    print("/$$$$$$ /$$                   /$$$$$$$                                      /$$      /$$ /$$   /$$     /$$             /$$     /$$                  /$$")
    print("|_  $$_/| $/                  | $$__  $$                                    | $$  /$ | $$|__/  | $$    | $$            |  $$   /$$/                 | $$")
    print("  | $$  |_//$$$$$$/$$$$       | $$  \ $$  /$$$$$$  /$$$$$$$   /$$$$$$       | $$ /$$$| $$ /$$ /$$$$$$  | $$$$$$$        \  $$ /$$//$$$$$$  /$$   /$$| $$)")
    print("  | $$    | $$_  $$_  $$      | $$  | $$ /$$__  $$| $$__  $$ /$$__  $$      | $$/$$ $$ $$| $$|_  $$_/  | $$__  $$        \  $$$$//$$__  $$| $$  | $$| $$")
    print("  | $$    | $$ \ $$ \ $$      | $$  | $$| $$  \ $$| $$  \ $$| $$$$$$$$      | $$$$_  $$$$| $$  | $$    | $$  \ $$         \  $$/| $$  \ $$| $$  | $$|__/")
    print("  | $$    | $$ | $$ | $$      | $$  | $$| $$  | $$| $$  | $$| $$_____/      | $$$/ \  $$$| $$  | $$ /$$| $$  | $$          | $$ | $$  | $$| $$  | $$    ")
    print(" /$$$$$$  | $$ | $$ | $$      | $$$$$$$/|  $$$$$$/| $$  | $$|  $$$$$$$      | $$/   \  $$| $$  |  $$$$/| $$  | $$          | $$ |  $$$$$$/|  $$$$$$/ /$$")
    print("|______/  |__/ |__/ |__/      |_______/  \______/ |__/  |__/ \_______/      |__/     \__/|__/   \___/  |__/  |__/          |__/  \______/  \______/ |__/")


def get_category(path):
    files = os.listdir(path)

    print("Choose a category...")
    
    for i, f in enumerate(files):
        full_path = path + "/" + f

        with open(full_path, 'r') as file:
            print(str(i) + ") " + file.readline().strip())

    choice = input("Enter selection: ")
    choice = int(choice)

    return path + "/" + files[choice]

def get_puzzle(file):
    #words = ["patriots", "soccer", "french fries", "larry the lobster"]

    with open(file, 'r') as f:
        words = f.read().splitlines()

    return random.choice(words).upper()

def check(word, solved, guesses):
    for i in range(len(word)):
        if word[i] in guesses or not word[i].isalpha():
            solved = solved[:i] + word[i] + solved[i+1:]

    return solved

def get_guess():
    while True:
        guess = input("Guess a letter: ")

        if len(guess) == 1 and guess.isalpha():
            return guess.upper()
        else:
            print("Invalid. Enter just 1 letter.")

        
def display_board(solved, guesses, strikes):

    if strikes == 0:
        print(" 0000000000000")
        print(" 0           0")
        print(" 0           ")
        print(" 0          ")
        print(" 0           ")
        print(" 0          ")
        print(" 0         ")
        print(" 0        ")
        print(" 0        ")  
        print(" 0      ")   
        print(" 0    ")    
        print(" 0  ")     
        print(" 0")
        print(" 0")
        print(" 0")
        print("0000000000000000000000 ") 
    elif strikes == 1:
        print("0000000000000 ")
        print("0           0")
        print("0           1")
        print("0          1 1")
        print("0           1")
        print("0          ")
        print("0         ")
        print("0")
        print("0  ")        
        print("0    ")     
        print("0      ")  
        print("0       ")
        print("0")
        print("0")
        print("00000000000000000000")
    elif strikes == 6:
        print("___________.._______")
        print("| .__________))______|")
        print("| | / /      ||")
        print("| |/ /       ||")
        print("| | /        ||.-''.")
        print("| |/         |/  _  \ ")
        print("| |          ||  `/,|")
        print("| |          (\\`_.'")
        print("| |         .-`--'.")
        print(" | |        /Y . . Y\ ")
        print("| |       // |   | \\")
        print("| |      //  | . |  \\")
        print("| |     ')   |   |   (`")
        print("| |          ||'||")
        print("| |          || ||")
        print("| |          || ||")
        print("| |          || ||")
        print(" | |         / | | \ ")
      
        
    print(solved + " [" + guesses + "]")
    
def play_again():
    while True:
        answer = input("Would you like to play again? ")

        if answer == 'no' or answer == 'n':
            return False
        elif answer == 'yes':
            return True

        print("What?!!! Just say yes or no.")

def play():
    puzzle_dir = 'puzzles'
    category_file = get_category(puzzle_dir)
    word = get_puzzle(category_file)
    solved = "-" * len(word)
    
    guesses = ""
    strikes = 0
    limit = 6
    
    solved = check(word, solved, guesses)
    display_board(solved, guesses, strikes)

    while word != solved and strikes < limit:
        letter = get_guess()

        if letter not in word:
            strikes += 1
            
        guesses += letter
        
        solved = check(word, solved, guesses)
        display_board(solved, guesses, strikes)

    if word == solved:
        print("You win!")
    else:
        print("You lose!")
                                                     


def main():
    show_start_screen()

    playing = True

    while playing:
        play()
        playing = play_again()

    show_end_screen()

# code execution begins here
if __name__ == "__main__":
    main()
