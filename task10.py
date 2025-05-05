# Нужно считать файл parameters.txt. 
# Это файл с настройками расчетной модели.
# Формат в файле следующий первое слово в строке - это ключ, 
# потом после пробела - значение (может быть строкой, числом, или набором чисел),
# все, что после символа "//" это комментарий  должно игнорироваться.
# Реализуйте считывание значений из файла и запись этих значений в словарь.
from os.path import split

ln =[]
dict = {}
l1, l2 = '', ''

i = 0
x = 0
with open('parameters.txt', encoding='utf-8') as f:
    while len(f.readline(-1)) != 0:
        ln += f.read()

while i != len(ln):
    l1 += ln[i]
    i += 1
    if i == len(ln):
        break
    if ln[i] == ' ':
        while ln[i] != '\n':
            i += 1
            l2 += ln[i]

l2 = (l2.split('\n'))
l1 = l1.split('\n')
while x != len(l1):
    if l1[x] == '':
        l1.pop(x)
        x -= 1
    x += 1
for i in range(len(l1)):
    dict[l1[i]] = l2[i].rstrip()

print(dict)
