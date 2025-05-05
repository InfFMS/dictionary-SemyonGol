# Даны два словаря. Напишите программу, которая объединит эти словари. 
# Если ключи встречаются в обоих исходных словарях, значения, 
# которые хранятся по этим ключам складываются.
# Пример:

# Первый словарь: {'a': 100, 'b': 200, 'c':300}
# Второй словарь: {'a': 300, 'b': 200, 'd':400}
# Результат: {'a': 400, 'b': 400, 'd': 400, 'c': 300}

A = {'a': 100, 'b': 200, 'c':300}
B = {'a': 300, 'b': 200, 'd':400, 'e': 37}
C = {}
AV = list(A.values())
BV = list(B.values())
AK = list(A.keys())
BK = list(B.keys())
for x in range(0, len(A)):
    for j in range(0, len(B)):
        if AK[x] == BK[j]:
            C[AK[x]] = AV[x] + BV[j]
            B.pop(BK[j])
            A.pop(AK[x])
            x -= 1
            j -= 1

AV = list(A.values())
BV = list(B.values())
AK = list(A.keys())
BK = list(B.keys())

for i in range(len(A)):
    C[AK[i]] = AV[i]
for k in range(len(B)):
    C[BK[k]] = BV[k]
print(C)