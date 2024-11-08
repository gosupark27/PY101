import random


VALID_CHOICES = ['rock', 'paper', 'scissors']

def prompt(message):
    print(f'==> {message}')

def display_winner():
    prompt(f'You chose {choice}, computer chose {computer_choice}')
    
    if ((choice == "rock" and computer_choice == "scissors") or
        (choice == "paper" and computer_choice == "rock") or
        (choice == "scissors" and computer_choice == "paper")):
        return "You win!"
    elif ((choice == "rock" and computer_choice == "paper") or
        (choice == "paper" and computer_choice == "scissors") or
        (choice == "scissors" and computer_choice == "rock")):
        return "Computer win!"
    else:
        return "It's a tie!"

answer = ' '

while answer[0] != 'n':
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input()

    computer_choice = random.choice(VALID_CHOICES)

    prompt(display_winner())

    while True:
        prompt("Do you want to play again? (y/n)")
        answer = input().lower()

        if answer.startswith('n') or answer.startswith('y'):
            break
        else:
            prompt("That's not a valid choice")
    
    if answer[0] == 'n':
        break