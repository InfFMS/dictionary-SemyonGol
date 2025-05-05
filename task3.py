# Напишите программу, которая получает на вход строку и подсчитывает, 
# сколько раз в ней встречается каждый символ (независимо от регистра).
# Результат нужно вывести без фигурных скобок
# Пример. 
# ввод:
# Абракадабра
# Вывод
# а-5 б-2 д-1 к-1 р-2

Dict ={}
j = 0
Num = ''

Inp = input()
Inp = Inp.lower()

for j in range(len(Inp)):
    c = 0
    a = Inp[j]
    for x in range(len(Inp)):
        if Inp[j] == Inp[x]:
            c += 1
            Inp.replace(Inp[j], ' ')
    Dict.__setitem__(a, c)
    if a == '':
        Dict.pop(a)

Ltr = list(Dict.keys())
Num = list(Dict.values())

for i in range(len(Dict)):
    if Ltr[i] == ' ':
        i += 1
        if i > len(Dict):
            break
    else:
        print(Ltr[i], ':', Num[i])
