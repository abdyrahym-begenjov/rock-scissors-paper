rutranslate={
    'Rock, Scissors, Paper': 'Камень, ножницы, бумага',
    'Enter the number of rounds for game (Number must be no even): ': 'Введите количество раундов игры (число не должно быть четным): ',
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
    'Enter to exit: ': 'Введите для выхода: '
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