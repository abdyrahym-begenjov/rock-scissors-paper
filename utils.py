from propython import *
from translator import *
from subprocess import run
from platform import system

def clear_screen():
    current_os=system()
    if current_os=='Windows':
        run(["cls"], shell=True)
    else:
        run(['clear'])

def enter_lang(data):
    print('English |  Русский')
    while True:
        chosen_language=input()
        chosen_language=chosen_language.title().strip()
        match chosen_language:
            case 'Русский':
                lang='ru'
                break
            case 'English':
                lang='en'
                break
            case _:
                continue
    
    data['language']=lang
    pywrite('data.json', data)
    return lang

def enter_name(lang, data):
    while True:
        name=input(translator('Enter your name: ', lang))
        if name!='':
            data['name']=name
            pywrite('data.json', data)
            return name
        
def draw_leaderboard(base, name, lang):
    try:
        a, b, c=[], [], []
        user=base[name]
        user1=list(user.items())
        user1.sort()
        base[name]=dict(user1)
        for i in base[name].values():
            a.append(str(i[0]))
            b.append(str(i[1]))
            c.append(str(i[2]))
        a=[f'{i:<8}|' for i in a]
        b=[f'{i:<8}|' for i in b]
        c=[f'{i:<8}|' for i in c]
        a=' '.join(a)
        b=' '.join(b)
        c=' '.join(c)
        name1=f'{name} |'
        line1=f'|{translator('NUMBER OF WINS POINTS |', lang):>30} {a:<6}'
        line2=f'|{name1:>30} {b:<6}'
        line3=f'|{translator('COMPUTER |', lang):>30} {c:<6}'
        line='-'*len(line1)
            
        print(line)
        print(line1)
        print(line)
        print(line2)
        print(line)
        print(line3)
        print(line)
    except KeyError:
        print(translator('You\'ve never played before. After your first game, you\'ll have a high score table.', lang))

def new_word(word, lang):
    word=word.strip().title()
    if lang=='ru':
        word=translator(word, 'en1')
    return word