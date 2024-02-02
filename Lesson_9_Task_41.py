# Задача 41. Дан массив, состоящий из целых чисел. Напишите программу, которая в данном массиве определить
# количество элементов, у которых два соседних и, при этом, оба соседних элемента меньше данного. Сначала 
# вводится число N - количество элементов в массиве Далее записаны N чисел - элементы массива. Массив состоит
# из целых чисел.

n = int(input('Please give me a number of list element q-ty: '))
list_1 = list()

for i in range(n):
    x = int(input('Please give me a number for list: '))
    list_1.append(x)

count = 0
for i in range(1, n-1):
    if list_1[i - 1] < list_1[i] > list_1[i + 1]:
        count += 1
print(count)
