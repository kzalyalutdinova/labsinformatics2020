import csv

def check_year(argument):
    return any(date in argument for date in years) or (years == [''])


def check_publishers(argument):
    return any(publisher in argument for publisher in publishers) or (publishers == [''])


def check_platforms(argument):
    return any(platform in argument for platform in platforms) or (platforms == [''])


def check_categories(argument):
    return any(category in argument for category in categories) or (categories == [''])


def check_genres(argument):
    return any(genre in argument for genre in genres) or (genres == [''])


def max_price(argument, game_price):
    return argument == '' or game_price <= float(argument)

def check_ratings(argument):
    return ((ratings == 'Да') and argument > 0) or (ratings == '')

print('Вводите данные через запятую. Если Вы хотите пропустить вопрос - нажмите Enter')

years = input('Укажите, игры каких годов Вас интересуют').split(',')
publishers = input('Укажите, игры каких разработчиков Вас интересуют').lower().split(',')
platforms = input('Укажите, какие платформы для игр Вас интересуют (mac, Linux, Windows)').lower().split(',')
categories = input('Укажите, какие категории игр Вы предпочитаете').lower().split(',')
genres = input('Укажите, какие жанры игр Вас интересуют').lower().split(',')
prices = input('Укажите, какая максимальная цена игры приемлема для Вас (напишите цену в долларах)')
ratings = input('Укажите, важен ли для Вас положительный рейтинг игры (ответьте "да" или "нет")').lower()

with open('steam.csv', encoding='utf-8') as file, \
        open('results.txt', 'w', encoding='utf-8') as out:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == 'appid':
            continue

        result_years = row[2].split('-')
        result_publishers = row[5].lower().split(';')
        result_platforms = row[6].lower().split(';')
        result_categories = row[8].lower().split(';')
        result_genres = row[9].lower().split(';')
        result_prices = float(row[17])
        result_ratings = int(row[12]) - int(row[13])

if (check_year(result_years) and check_publishers(result_publishers) and check_platforms(result_platforms)
        and check_categories(result_categories) and check_genres(result_genres) and max_price(result_prices)
        and check_ratings(result_ratings)):
            out.write(row[1] + '\n')