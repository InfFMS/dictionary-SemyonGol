# Напишите программу, которая получает на вход строку чисел, разделенных пробелами,
#и формирует словарь, в котором ключами служат числа,
#а значениями – слово "четное" или "нечетное".

Odd = []
Dict = {}
N = input()
N = N.split()
for i in range(len(N)):
    N[i] = int(N[i])
    if N[i]%2 == 0:
        Odd += ['Even']
    else:
        Odd += ['Odd']
    Dict.__setitem__(N[i], Odd[i])
print(Dict)