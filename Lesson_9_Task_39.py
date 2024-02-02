# Задача № 39. Даны два массива чисел. Требуется вывести те элементы первого массива
# (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь ВВОДИТ 
# число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число М - 
# количество элементов во втором массиве. Затем элементы второго массива.
n = int(input('Please give me a number of list element q-ty: '))
list_1 = list()

for i in range(n):
    x = int(input('Please give me a number for list: '))
    list_1.append(x)

m = int(input('Please give me a number of 2nd list element q-ty: '))
list_2 = list()

for i in range(m):
    x = int(input('Please give me a number for list: '))
    list_2.append(x)

count = 0
for i in range(n):
    for j in range(m):
        if list_1[i] == list_2[j]:
            count += 1
    if count == 0:
        print(list_1[i])
    count = 0
