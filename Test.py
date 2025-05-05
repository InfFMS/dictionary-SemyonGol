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
    dict[l1[i]] = l2[i]
print(dict)
print(l2)
print(l1)
