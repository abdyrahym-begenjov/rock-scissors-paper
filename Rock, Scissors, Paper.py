from random import choice
from time import sleep
from translator import *
from propython import pyread, pywrite
from utils import *

base=pyread('base.json')
data=pyread('data.json')

name=data['name']
lang=data['language']

if lang=='':
    lang=enter_lang(data)
    clear_screen()

if name=='':
    name=enter_name(lang, data)
    clear_screen()

while True:
    print(translator('Rock, Scissors, Paper', lang))
    print(f'{translator('Creator: Abdyrahym Begenjov', lang)}     (GitHub: abdyrahym-begenjov)')
    print(translator('Game      Rules      Highscores      Settings      Exit', lang))
    mode=input(translator('Choose a game mode: ', lang))
    mode=new_word(mode, lang)
    if name not in base:
        base[name]=[0, 0]
    clear_screen()
    match mode:
        case 'Game':
            while True:
                num=input(translator('How many wins are we playing to?: ', lang))
                try:
                    num=int(num)
                    if num<=0:
                        print(translator('The number must not be less than or equal to zero!!!', lang))
                    else:
                        break
                except ValueError:
                    print(translator('Error!!!', lang))

            print(translator('Loading...', lang))
            sleep(2)
            clear_screen()

            words=[translator('Rock', lang), translator('Scissors', lang), translator('Paper', lang)]
            up=0
            cp=0

            while True:
                user=input(f'{translator('Enter the word: ', lang)}')
                user=new_word(user, lang)
                computer=choice(words)
                computer=new_word(computer, lang)
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
                    base[name][1]+=num
                    break
                elif up==num:
                    print(translator('You win!!!', lang))
                    base[name][0]+=num
                    break
            pywrite('base.json', base)

            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Rules':
            if lang=='ru':
                rules=pyread('ru_rules.txt')
            else:
                rules=pyread('en_rules.txt')
            print(rules)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Highscores':
            draw_leaderboard(base, lang)
            end=input(translator('Enter to exit mode: ', lang))
            clear_screen()

        case 'Settings':
            while True:
                print(f'{translator('Name', lang)}: {data['name']}')
                print(f'{translator('Language', lang)}: {data['language']}')
                change=input(translator('Do you want to change parameters (Enter \"Name\" or \"Language\"): ', lang))
                change=new_word(change, lang)
                match change:
                    case 'Name':
                        name=enter_name(lang, data)
                        clear_screen()
                    case 'Language':
                        lang=enter_lang(data)
                        clear_screen()
                    case _:
                        break
            clear_screen()

        case 'Exit':
            exit_confirm=input(translator('Do you want to exit (\"Yes\" or \"No\"): ', lang))
            exit_confirm=new_word(exit_confirm, lang)
            if exit_confirm=='No':
                clear_screen()
            else:
                print(translator('Goodbye!!!', lang))
                input(translator('Enter to exit: ', lang))
                break
        case _:
            clear_screen()