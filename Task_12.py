# Заполните массив элементами арифметической прогрессии. Ее первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.Формула для
# получения n-го члена прогрессии:a = a1 +(n-1) *d.каждое число вводится с 
# новой строки.

n = int(input('Введите количество элементов: '))
a1 = int(input('Введите первый элемент: '))
d = int(input('задайте разность: '))
for i in range(n):
    print(a1 + i * d, end = ' ')