# Задача 8: Требуется определить, можно ли от шоколадки размером n х m долек отломить к долек, если 
# разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# 324 -> yes
# 321-> no

n = int(input())
m = int(input())
k = int(input())

if k < m*n and (k%m==0 or k%n==0):
    print('YES')
else:
    print('NO')