import random
from time import *

def hangman():

    global streak
    streak = 0

    def difficulty():
        while True:
            diff = input('Choose your difficulty (E/M/H): ')
            if diff == 'E' or diff == 'e': return 10
            elif diff == 'M' or diff == 'm': return 6
            elif diff == 'H' or diff == 'h': return 4
            else: print("Enter a valid input!\n")

    def setup():
        f = open("dictionary.txt",'r')
        words = (f.read()).split('\n')
        diff = difficulty()

        while True:
            word = random.choice(words)
            if diff == 10 and len(word)<=4: #easy
                break
            if diff == 6 and 5 <= len(word) <= 6: #medium
                break
            if diff == 4 and len(word)>6:  #hard
                break

        return[diff, word]

    def play():
        print("\n\n-------------------\nWelcome to Hangman! \n")
        setting = setup()
        guesses = setting[0]
        answer = setting[1]

        print("You have ", guesses, 'attempts to guess the right answer!')
        guess = ('_ ' * len(answer)).split()
        print("The answer is : ", ' '.join(guess), '\n')
        incorrect = []

        while ''.join(guess) != answer and guesses != 0:
            attempt = input("Enter guess:")

            if attempt.isalpha() == False or len(attempt) > 1:
                print("Please enter a valid letter!\n")

            elif attempt in answer:
                if attempt in guess:
                    print("You have already guessed that!\n")
                for letter in range(len(answer)):
                    if answer[letter] == attempt:
                        guess[letter] = attempt
                print(' '.join(guess),'\n')

            elif attempt in incorrect:
                print("You have already guessed that!\n")

            else:
                incorrect.append(attempt)
                guesses -= 1
                print("Incorrect guesses: ", ', '.join(incorrect),'\n','You have', guesses, 'guesses remaining.\n')

        if ''.join(guess) == answer:
            print("Congrats, yon won!")
            return True
        else:
            print("Game over! The correct answer was", answer, '.')
            return False

    def main():
        global streak
        x = play()

        if x:
            streak += 1
            print("Streak: ", streak)
        else:
            streak = 0
            print("Streak: ", streak)

        x = input("\nDo you wanna play again? (Y/N)")
        if x == 'Y' or x == 'y':
             main()

        else:
            print("\nThanks for playing!")
            sleep(1)

    main()

hangman()