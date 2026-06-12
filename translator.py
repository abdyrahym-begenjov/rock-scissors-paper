rutranslate={
    'Rock, Scissors, Paper': 'Камень, ножницы, бумага',
    'How many wins are we playing to?: ': 'До скольких побед играем?: ',
    'Rock': 'Камень',
    'Scissors': 'Ножницы',
    'Paper': 'Бумага',
    'Enter the word: ': 'Введите слово: ',
    'Error!!!': 'Ошибка!!!',
    'Computer': 'Компьютер',
    'User': 'Пользователь',
    'Computer wins': 'Компьютер побеждает',
    'Game Over!!!': 'Игра окончена!!!',
    'You win!!!': 'Вы победили!!!',
    'This word has already been used.': 'Это слово уже было использовано.',
    'Creator: Abdyrahym Begenjov': 'Создатель: Абдырахым Бегенджов',
    'Enter to start game: ': 'Нажмите, чтобы начать игру: ',
    'Loading...': 'Загрузка...',
    'Enter to exit: ': 'Введите для выхода: ',
    'Enter your name: ': 'Введите свое имя: ',
    'Enter to exit mode: ': 'Войдите в режим выхода: ',
    'Game      Rules      Highscores      Settings      Exit': 'Игра      Правила      Рекорды      Настройки      Выход',
    'Choose a game mode: ': 'Выберите режим игры: ',
    'Do you want to change parameters (Enter \"Name\" or \"Language\"): ': 'Хотите ли вы изменить параметры (введите \"Имя\" или \"Язык\"): ',
    'Do you want to exit (\"Yes\" or \"No\"): ': 'Вы хотите завершить (\"Да\" или \"Нет\"): ',
    'Goodbye!!!': 'До свидания!!',
    'Name': 'Имя',
    'Language': 'Язык',
    'Return': 'Вернуться',
    'Game': 'Игра',
    'Rules': 'Правила',
    'No': 'Нет',
    'Highscores': 'Рекорды',
    'Settings': 'Настройки',
    'Exit': 'Выход', 
    'NAME |': 'ИМЯ |',
    'OVERALL RESULT': 'ОБЩИЙ РЕЗУЛЬТАТ',
    'VICTORIES': 'ПОБЕДЫ',
    'DEFEATS': 'ПОРАЖЕНИЯ',
    'LEADERBOARD:': 'ЛИДЕРБОРД:',
    'The number must not be less than or equal to zero!!!': 'Число не должно быть меньше или равной нулю!!!'
             }


entranslate={j: i for i, j in rutranslate.items()}


def translator(word, language):
    match language:
        case 'en':
            return word
        case 'en1':
            if word not in entranslate:
                return 'Error!!!'
            return entranslate[word]
        case 'ru':
            return rutranslate[word]
        case _:
            return '???'