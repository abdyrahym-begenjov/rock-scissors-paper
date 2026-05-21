from random import choice
from time import sleep
from translator import *
from propython import *
from subprocess import run
from platform import system

base=pyread('base.json')
data=pyread('data.json')

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_name():
    while True:
        name=input(translator('Enter your name: ', lang))
        if name!='':
            data['name']=name
            pywrite('data.json', data)
            return name

def enter_lang():
    print('English |  Русский')
    while True:
        chosen_language=input()
        chosen_language=chosen_language.title().strip()
        if chosen_language=='English' or chosen_language=='Русский':
            break

    match chosen_language:
        case 'Русский':
            lang='ru'
        case 'English':
            lang='en'
    data['language']=lang
    pywrite('data.json', data)
    return lang

name=data['name']
lang=data['language']

if lang=='':
    lang=enter_lang()

if name=='':
    name=enter_name()

while True:
    print(translator('Rock, Scissors, Paper', lang))
    print(f'{translator('Creator: Abdyrahym Begenjov', lang)}     (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Records      Settings      Exit', lang))
    mode=input(translator('Choose a game mode: ', lang))
    mode=mode.title().strip()
    if lang=='ru':
        mode=translator(mode, 'en1')
    match mode:
        case 'Game':
            start=input(translator('Enter to start game: ', lang))

            while True:
                num=input(translator('Enter the number of rounds for game (Number must be no even): ', lang))
                try:
                    num=int(num)
                    if num%2!=0:
                        break
                    else:
                        print(translator('Error!!!', lang))
                except ValueError:
                    print(translator('Error!!!', lang))

            if str(num) not in base:
                base[str(num)]=[num, 0, 0]

            print(translator('Loading...', lang))
            sleep(2)

            words=[translator('Rock', lang), translator('Scissors', lang), translator('Paper', lang)]
            up=0
            cp=0

            while True:
                user=input(f'{translator('Enter the word: ', lang)}')
                user=user.title().strip()
                if lang=='ru':
                    user=translator(user, 'en1')
                computer=choice(words)
                if lang=='ru':
                    computer=translator(computer, 'en1')
                match user, computer:
                    case ('Rock', 'Paper') | ('Paper', 'Scissors') | ('Scissors', 'Rock'):
                        cp+=1
                    case ('Paper', 'Rock') | ('Scissors', 'Paper') | ('Rock', 'Scissors'):
                        up+=1
                    case ('Rock', 'Rock') | ('Paper', 'Paper') | ('Scissors', 'Scissors'):
                        pass
                    case _:
                        print(translator('Error!!!', lang))
                        continue
                print(f'{translator('Computer', lang)}: {translator(computer, lang)}')
                print(f'{translator('User', lang)}: {up}      {translator('Computer', lang)}: {cp}')
                if cp==num:
                    print(translator('Computer wins', lang))
                    print(translator('Game Over!!!', lang))
                    base[str(num)][2]+=1
                    break
                elif up==num:
                    print(translator('You win!!!', lang))
                    base[str(num)][1]+=1
                    break
            pywrite('base.json', base)

            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()
        case 'Records':
            a, b, c=[], [], []
            for i in base.values():
                a.append(str(i[0]))
                b.append(str(i[1]))
                c.append(str(i[2]))
            a=f'{' ':<8}| '.join(a)
            b=f'{' ':<8}| '.join(b)
            c=f'{' ':<8}| '.join(c)
            line1=f'|{'NUMBER OF ROUND |':>20} {a} {' ':<6}|'
            line2=f'|{'HUMAN |':>20} {b} {' ':<6}|'
            line3=f'|{'COMPUTER |':>20} {c} {' ':<6}|'
            line='-'*len(line1)
            
            print(line)
            print(line1)
            print(line)
            print(line2)
            print(line)
            print(line3)
            print(line)

            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()
        case 'Settings':
            while True:
                print(f'{translator('Name', lang)}: {data['name']}')
                print(f'{translator('Language', lang)}: {data['language']}')
                change=input(translator('Do you want to change parameters (Enter \"Name\" or \"Language\"): ', lang))
                change=change.title().strip()
                if lang=='ru':
                    change=translator(change, 'en1')
                match change:
                    case 'Name':
                        name=enter_name()
                        clear_screen()
                    case 'Language':
                        lang=enter_lang()
                        clear_screen()
                    case _:
                        break
            clear_screen()
        case 'Exit':
            exit_confirm=input(translator('Do you want to exit: ', lang))
            exit_confirm=exit_confirm.title().strip()
            if lang=='ru':
                exit_confirm=translator(exit_confirm, 'en1')
            if exit_confirm=='Return':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break
        case _:
            clear_screen()