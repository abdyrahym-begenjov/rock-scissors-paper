from random import choice

words=['Rock', 'Scissors', 'Paper']
up=0
cp=0

num=int(input('Enter the number of rounds for game: '))
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
    print(f'{'Computer'}: {computer}')
    print(f'{'User'}: {up}      {'Computer'}: {cp}')
    if cp==num:
        print('Computer wins')
        print('Game Over!!!')
        break
    elif up==num:
        print('You win!!!')
        break