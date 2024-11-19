# Даны два массива чисел. ТРебуется вывести те элементы первого массива(в том порядке
# в каком они идут в первом массиве), которых нет во втором массиве. Пользователь
# вводит число N - количество элементов в первом массиве, затем N чисел-
# элементы массива.Затем число  M- количество элементов во втором массиве.
# затем элементы второго массива.

n = int(input())
list1 = list()
for i in range(n):
    x = int(input())
    list1.append(x)

m = int(input())
list2 = list()
for i in range(m):
    x = int(input())
    list2.append(x)

count = 0
for i in range(n):
    for j in range(m):
        if list1[i] == list2[j]:
            count += 1
    if count == 0:
         print(list1[i])
    count = 0




