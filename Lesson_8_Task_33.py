# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на
# максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные - на минимальные.
# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1 
n = int(input('Please give me a number: '))

list_1 = list()
for i in range(n):
    x = int(input())
    list_1.append(x)

max_n = max(list_1) # Функция определения максимального числа в списке
min_n = min(list_1) # Функция определения минимального числа в списке
print('Maximum is', max_n)

for i in range(len(list_1)):
    if list_1[i] == max_n:
        list_1[i] = min_n

print(list_1)
