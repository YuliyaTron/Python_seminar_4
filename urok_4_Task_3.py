# Задайте последовательность чисел. 
# Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.

import random
n = int(input("Введите колличество чисел последовательности: "))

list = []
for i in range(n):
    list.append(random.randint(0, 20))
print(list)

new_list = []
for i in list:
    if i not in new_list:
        new_list.append(i)
print(new_list)

