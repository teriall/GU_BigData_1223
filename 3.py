# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
# Напишите решения через list и через dict.

# user_month = int(input('Введите номер месяца в виде целого числа от 1 до 12: '))
# season = ['зима', 'весна', 'лето', 'осень']
#
# if user_month <= 2 or user_month >= 11:
#     print(f'На дворе {season[0]}')
# elif 3 <= user_month <= 5:
#     print(f'На дворе {season[1]}')
# elif 6 <= user_month <= 8:
#     print(f'На дворе {season[2]}')
# else:
#     print(f'На дворе {season[3]}')

user_month = int(input('Введите номер месяца в виде целого числа от 1 до 12: '))
season = {1: 'зима', 2: 'весна', 3: 'лето', 4: 'осень'}

if user_month <= 2 or user_month >= 11:
    print(f'На дворе {season.get(1)}')
elif 3 <= user_month <= 5:
    print(f'На дворе {season.get(2)}')
elif 6 <= user_month <= 8:
    print(f'На дворе {season.get(3)}')
else:
    print(f'На дворе {season.get(4)}')