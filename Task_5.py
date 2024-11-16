# Напишите программу, которая на вход принимает два числа А и В, и возводит
# число А в целую степень В с помощью рекурсии.
b = int(input())
a = int(input())
def degree_num(a,b):
    if b == 0:
        return 1
    return a * degree_num(a,b - 1)

print(degree_num(a,b))



