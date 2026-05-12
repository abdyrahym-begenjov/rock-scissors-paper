from random import choice
from time import sleep
from translator import *

print('en |  ru')
while True:
    lan=input()
    if lan=='en' or lan=='ru':
        break

print(translator('Rock, Scissors, Paper', lan))
print(f'{translator('Creator: Abdyrahym Begenjov', lan)}     (GitHub: abdyrahym-begenjov)')
start=input(translator('Enter to start game: ', lan))
print(translator('Loading...', lan))
sleep(2)

words=[translator('Rock', lan), translator('Scissors', lan), translator('Paper', lan)]
up=0
cp=0

while True:
    num=input(translator('Enter the number of rounds for game (Number must be no even): ', lan))
    try:
        num=int(num)
        if num%2!=0:
            break
        else:
            print(translator('Error!!!', lan))
    except ValueError:
        print(translator('Error!!!', lan))

while True:
    user=input(f'{translator('Enter the word: ', lan)}')
    user=user.title().strip()
    if lan=='ru':
        user=translator(user, 'en1')
    computer=choice(words)
    if lan=='ru':
        computer=translator(computer, 'en1')
    match user, computer:
        case ('Rock', 'Paper') | ('Paper', 'Scissors') | ('Scissors', 'Rock'):
            cp+=1
        case ('Paper', 'Rock') | ('Scissors', 'Paper') | ('Rock', 'Scissors'):
            up+=1
        case ('Rock', 'Rock') | ('Paper', 'Paper') | ('Scissors', 'Scissors'):
            pass
        case _:
            print(translator('Error!!!', lan))
            continue
    print(f'{translator('Computer', lan)}: {translator(computer, lan)}')
    print(f'{translator('User', lan)}: {up}      {translator('Computer', lan)}: {cp}')
    if cp==num:
        print(translator('Computer wins', lan))
        print(translator('Game Over!!!', lan))
        break
    elif up==num:
        print(translator('You win!!!', lan))
        break

end=input(translator('Enter to exit: ', lan))