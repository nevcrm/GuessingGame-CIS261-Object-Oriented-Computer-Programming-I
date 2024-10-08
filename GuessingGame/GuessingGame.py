
#// Name: Marcus Bracken
#// Course: CIS261-Object-Oriented Computer Programming I
#// Lab: Guessing Game

import random

def display_heading():
    print("Guess the number!")
    
def play_guessing_game():
    limit = int(input("Enter the limit: "))
    
    print(f"I'm thinking of a number from 1 to {limit}")
    
    number_to_guess = random.randint(1, limit)

    guess = None
    number_of_tries = 0

    while guess != number_to_guess:
        guess = int(input("Your guess: "))
        number_of_tries += 1
    
        if guess < number_to_guess:
            print("Too low.")
        elif guess > number_to_guess:
            print("Too high.")
        else:
            print(f"You guessed it in {number_of_tries} tries.")
        
def main():
    play_again = 'y'
    while play_again.lower() == 'y':
        display_heading()
        play_guessing_game()
        play_again = input("Would you like to play again? (y/n): ")
    print("Bye!")
   
if __name__ == "__main__":
    main()


