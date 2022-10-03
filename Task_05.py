# Задание 5 Реализуйте алгоритм перемешивания списка.


import random
def mix_list(list_original):
    list = list_original[:]
    list_ = len(list)
    for i in range(list_):
        index_ = random.randint(0, list_ - 1)
        temp = list[i]
        list[i] = list[index_]
        list[index_] = temp
    return list


list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
mixed_list = mix_list(list)
print('Исходный список: ')
print(list)
print('Перемешанный список: ')
print(mixed_list)