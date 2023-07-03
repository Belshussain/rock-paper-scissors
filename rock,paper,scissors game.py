import random

user_wins = 0
computer_wins = 0

options = ["rock", "paper", "scissors"]

YN = input('Would you like to play rock/paper/scissors? ')

if YN.lower() == 'yes':
    print('Lets play! ')
else:
    quit()


while True:
    user_input = input('Enter Rock/Paper/Scissors or Q to quit:  ').lower()
    if user_input == 'q':
        break

    if user_input not in options:
        print('Enter a valid answer ')
        continue

    random_number = random.randint(0,2)
    #rock = 0, paper = 1, scissors = 2
    computer_answer = options[random_number]
    print('Computer chose ',computer_answer,  '.')

    if user_input == 'rock' and computer_answer == 'scissors':
        print('You have won! ')
        user_wins += 1
        
    elif user_input == 'paper' and computer_answer == 'rock':
        print('You have won! ')
        user_wins += 1
        
    elif user_input == 'scissors' and computer_answer == 'paper':
        print('You have won! ')
        user_wins += 1
        
    elif user_input == computer_answer:
        print('Seems its a draw! ')

    else:
        print('You have lost! ')
        computer_wins +=1

print('You won ', user_wins , 'times.')
print('The computer won ', computer_wins, 'times.')
print('It was a good game! Goodbye.')
