# Представьте, что вы шпионы)
# Придумайте шифр, в котором буквы заменяются на какие-то символы
# и реализуйте шифроватор и дешифроватор

# Шифр: каждой букве русского алфавита соответствует верхняя правая буква на клавиатуре.
# Причем, если следующая буква есть как в английской азбуке, так и в русской,
# то ей соответствует заглавная буква русского алфавита на той же кнопке, иначе: английского (кроме Я).
# Если сверху справа нет буквы (цифра, скобка) пишем или цифру, или ту же букву
newLine = ''
code = {"А": "Е", "Б": "L", "В": "R", "Г": "8", "Д": "P", "Е": "6", "Ж": "Ж",
        "З": '-', "И": "Р", "Й": '2', 'К': '5', "Л": "Щ", "М": "G", "Н": '7',
        "О": "I", "П": "Y", "Р": "U", "С": "F", "Т": "J", "У": "4", "Ф": "W",
        "Х": "Х", "Ц": "3", "Ч": "D", "Ш": "9", "Щ": "0", "Ъ": "Ъ", "Ы": "У",
        "Ь": "Л", "Э": "Э", "Ю": "Ю", "Я": "Ы"}
deCode = {"Ж" :"Ж" ,"6" :"Е" ,"P" :"Д" ,"8" :"Г" ,"R" :"В" ,"L" :"Б" ,"Е" :"А",
        '7' :"Н" ,"G" :"М" ,"Щ" :"Л" ,'5' :'К' ,'2' :"Й" ,"Р" :"И" ,'-' :"З",
        "W" :"Ф" ,"4" :"У" ,"J" :"Т" ,"F" :"С" ,"U" :"Р" ,"Y" :"П" ,"I" :"О",
        "У" :"Ы" ,"Ъ" :"Ъ" ,"0" :"Щ" ,"9" :"Ш" ,"D" :"Ч" ,"3" :"Ц" ,"Х" :"Х",
        "Ы" :"Я" ,"Ю" :"Ю" ,"Э" :"Э" ,"Л" :"Ь"}

print("Выберите: 1 - зашифровать, 2 - дешифровать: ", end=' ')
key = int(input())

if key == 1:
        print('Введите то, что хотите зашифровать: ', end=' ')
        line = input()
        line = line.upper()
        for x in range(len(line)):
                newLine += str(code[line[x]])
        print(newLine)
elif key == 2:
    print('Введите то, что хотите дешифровать: ', end=' ')
    line = input()
    line = line.upper()
    for x in range(len(line)):
        newLine += str(deCode[line[x]])
    print(newLine)