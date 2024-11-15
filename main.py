# Модули

# первый способ импортирования модуля:
# import modul1
# print(modul1.max1(5, 9))

# второй способ импортирования модуля:
# from modul1 import max1
# print(max1(5, 9))

# если я хочу вызвать функцию из модуля, но его название слишком длинное и
# я хочу его переименовать для удобства:
# import modul1 as m1

# print(m1.max1(5, 9))

# from modul1 import * - означает, что я хочу вызвать абсолютно все функции
# из модуля.

# Рекурсии
# def fib(n):
#     if n in [1,2]:# базис(выход из рекурсии)Важно устанавливать базис во избежание переполонения стека.
#         return 1  
#     return fib(n - 1) + fib(n - 2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

#Быстрая сортировка
# def quick_sort(array):
#     if len(array) <= 1: # если длина массива меньше либо равна 1
#         return array    # то возвращаем массив как есть, без обработки
#     else:
#         pivot = array[0] # берем первый элемент как опорный
#     less = [i for i in array[1:] if i <= pivot] # если опорный объект больше текущего, то добавляем элемент в правую часть
#     greater = [i for i in array[1:] if i > pivot] # если опорный объект меньше текущего, то добавляем элемент в левую часть
#     return quick_sort(less) + [pivot] + quick_sort(greater) # отправляем на

# print(quick_sort([14,5,9,6,33,58,7,5,2,7]))

# #Cортировка слиянием(разбиение по парам, потом из них составляются новые пары,пары пар и т.д. где значения идут в порядке возрастания)
# def merge_sort(nums):
#     if len(nums) > 1:
#         mid = len(nums) // 2
#         left = nums[:mid]
#         right = nums[mid:]
#         merge_sort(left)
#         merge_sort(right)
#         i = j = k = 0
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 nums[k] = left[i]
#                 i += 1
#             else:
#                 nums[k] = right[j]
#                 j+= 1
#             k += 1
#         while i < len(left):
#             nums[k] = left[i]
#             i += 1
#             k += 1
#         while j < len(right):
#             nums[k] = right[j]
#             j += 1
#             k += 1

# list_1 = [1,5,6,9,8,7,2,1,55,2,4]
# merge_sort(list_1)
# print(list_1)