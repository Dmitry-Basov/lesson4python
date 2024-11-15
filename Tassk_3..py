# напишите функцию, которая принимает одно число и проверяет, является ли оно
# простым

def prime(n):
    flag = True
    i = 2
    while i < n and flag:
        if n % i == 0:
            flag = False
            break
        i += 1
    if flag:
        return 'yes'
    else:
        return 'no'
n = int(input())
print(prime(n))
        