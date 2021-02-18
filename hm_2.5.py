# Реализовать структуру «Рейтинг», представляющую собой
# не возрастающий набор натуральных чисел.
# У пользователя необходимо запрашивать новый элемент рейтинга.
# Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться
# после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Набор натуральных чисел можно задать непосредственно в коде,
# например, my_list = [7, 5, 3, 3, 2].

# my_list = [7, 5, 3, 3, 2]
# print(f"Рейтинг - {my_list}")
# digit = int(input("Введите число (111 - выход) "))
#
# while digit != 111:
#     for el in range(len(my_list)):
#         if my_list[el] == digit:
#             my_list.insert(el + 1, digit)
#             break
#         elif my_list[0] < digit:
#             my_list.insert(0, digit)
#         elif my_list[-1] > digit:
#             my_list.append(digit)
#         elif my_list[el] > digit and my_list[el + 1] < digit:
#             my_list.insert(el + 1, digit)
#
#     print(f"текущий список - {my_list}")
#     digit = int(input("Введите число "))

# def permutation(a, value):
#     max_value = max(a)
#     if value > max_value:
#         a.insert(0, value)
#     elif value in a:
#         a.insert(a.index(value), value)
#     else:
#         a.append(value)
#
#
# my_list = [7, 5, 3, 3, 2]
# print(my_list)
# permutation(my_list, 3)
# print(my_list)
# permutation(my_list, 8)
# print(my_list)
# permutation(my_list, 1)
# print(my_list)

num = int(input("Enter number: "))
my_list = [7, 4, 3, 2]
c = my_list.count(num)
for el in my_list:
    if c > 0:
        i = my_list.index(num)
        my_list.insert(i + c, num)
        break
    else:
        if num > el:
            j = my_list.index(el)
            my_list.insert(j, num)
            break
        elif num < my_list[len(my_list) - 1]:
            my_list.append(num)
print(my_list)