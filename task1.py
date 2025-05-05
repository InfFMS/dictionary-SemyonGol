# Напишите программу, которая получает на вход две строки, и формирует из них словарь. 
# Ключами служат слова из первой строки, значениями – целые числа из второй.
# Пример ввода
# яблоки сливы груши персики манго киви апельсины
# 34 56 23 89 55 32 11

Dict1, Dict2 = [], []
Dict = {}
c = 0

print('Enter keys: ', sep="\n")
Str1 = input()
while Str1 != '':
    Dict1 += [Str1]
    Str1 = input()
    c += 1

print('Enter values: ', sep="\n")
Str2 = int(input())
for i in range(0, c):
    Dict.__setitem__(Dict1[i], Str2)
    Str2 = input()

print(Dict)
