# Задача Nº35. Решение задачи
# Напишите функцию, которая принимает одно число и проверяет, является ли оно простым
# Напоминание: Простое число - это число, которое имеет 2 делителя: 1 и п (само число)
# Input: 5
# Output: yes
def prime(n):
    flag = True
    i = 2
    while i < n and flag:
        if n % i == 0:
            flag = False
        i += 1    
    if flag:
        return 'yes'
    else:
        return 'no'
    
n = int(input('Please give me a number: '))
print(prime(n))