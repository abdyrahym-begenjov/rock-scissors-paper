from random import choice
from time import sleep

print('Rock, Scissors, Paper')
print('Creator: Abdyrahym Begenjov     (GitHub: abdyrahym-begenjov)')
start=input('Enter to start: ')
print('Loading...')
sleep(2)
words=['Rock', 'Scissors', 'Paper']
up=0
cp=0
while True:
    num=(input('Enter the number of rounds for game (Number must be no even): '))
    try:
        num=int(num)
        if num%2!=0:
            break
        else:
            print('Error!!!')
    except ValueError:
        print('Error!!!')

while True:
    user=input(f'{'Enter the word: '}')
    user=user.title().strip()
    computer=choice(words)
    match user, computer:
        case ('Rock', 'Paper') | ('Paper', 'Scissors') | ('Scissors', 'Rock'):
            cp+=1
        case ('Paper', 'Rock') | ('Scissors', 'Paper') | ('Rock', 'Scissors'):
            up+=1
        case ('Rock', 'Rock') | ('Paper', 'Paper') | ('Scissors', 'Scissors'):
            pass
        case _:
            print('Error!!!')
            continue
    print(f'Computer: {computer}')
    print(f'User: {up:<10} Computer: {cp}')
    if cp==num:
        print('Computer wins')
        print('Game Over!!!')
        break
    elif up==num:
        print('You win!!!')
        break

end=input('Enter to exit: ')