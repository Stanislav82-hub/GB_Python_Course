# Задача 18: Требуется найти в массиве А[1..N] самый близкий по величине элемент к заданному числу Х.
# Пользователь в первой строке вводит натуральное число N - количество элементов в массиве. В последующих
# строках записаны N целых чисел А. Последняя строка содержит число х

n = int(input("Введите колличество элементов массива: "))
arr = list(map(int, input("Введите элемент массива: ").split()))
x = int(input("Введите число 'x' : "))
count = 0

min = abs(x - arr[0])
index = 0
for i in range(1, n):
    count = abs(x - arr[i])
    if count < min:
        min = count
        index = i
print(arr[index])        