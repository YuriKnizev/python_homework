# Пользователь вводит месяц в виде целого числа от 1 до 12.
# Сообщить к какому времени года относится месяц (зима, весна,
# лето, осень).
# Напишите решения через list и через dict.

list = ['winter', 'spring', 'summer', 'autumn']
dict = {1 : 'winter', 2 : 'spring', 3 : 'summer', 4 : 'autumn'}
m = int(input("Введите месяц по номеру:  "))

if m == 1 or m == 2 or m == 12:
    print(dict.get(1))
    print(list[0])
elif m == 3  or m == 4 or m == 5:
    print(dict.get(2))
    print(list[1])
elif m == 6 or m == 7 or m ==8:
    print(dict.get(3))
    print(list[2])
elif m == 9 or m == 10 or m ==11:
    print(dict.get(4))
    print(list[3])
else:
    print('Неверный ввод!')

    # seasons = {'Winter': (1, 2, 12),
    #            'Sping': (3, 4, 5),
    #            'Summer': (6, 7, 8),
    #            'Autumn': (9, 10, 11)}
    #
    # month = int(input('Введите номер месяца: '))
    # for key in seasons.keys():
    #     if month in seasons[key]:
    #         print(key)


