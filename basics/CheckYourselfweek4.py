#1) Создайте функцию, которая будет принимать 2 числа, складывать их и возвращать результат сложения.
def numar(num1, num2):
    return num1 + num2
result = numar(5, 7)
print(result)
'--------------------------------------------'
#2) Создайте функцию, которая принимает два обязательных параметра. Задача этой функции выводить тип принятых аргументов.
def chop(arg1, armatura, arma3):
    print(type(arg1))
    print(type(armatura))
    print(type(arma3))
chop(5, 'Hello', [78])
'----------------------------------------------'
#3) Напишите функцию, которая принимает список чисел и возвращает их произведение.
def mult(numb):
    result = 1
    for num in numb:
        result *= num
    return result
numbers_list = [2, 3, 4]
result = mult(numbers_list)
print(result)
'--------------------------------------------------'''
#4) Напишите функцию, которая принимает строку и выводит количество гласных,согласных букв и остальных символов. Используйте только кириллические символы
def countro(inputro_string):
    vam = set('аеёиоуыэюя')
    con = set('бвгджзйклмнпрстфхцчшщ')
    
    vowels = sum(1 for char in inputro_string.lower() if char in vam)
    consonants = sum(1 for char in inputro_string.lower() if char in con)
    other = len(inputro_string) - vowels - consonants
    
    print(f"Гласных: {vowels}")
    print(f"Согласных: {consonants}")
    print(f"Прочие символы: {other}")

input_str = 'Пример строки'
countro(input_str)
'--------------------------------------------------'
#5) Дан список из имён. Найдите самое длинное имя из списка функцией reduce.
from functools import reduce
names = ['Alice', 'Bob', 'Charlie', 'David', 'Eva']
long_name = reduce(lambda x, y: x if len(x) >= len(y) else y, names)
print(long_name)
'-------------------------------------------------------------'
#6) Дана глобальная переменная num со значением 3. Напишите функцию mul которая
#будет возвращать квадрат этой переменной и записывать результат в глобальную
#переменную num. Вызовите функцию три раза, и распечатайте переменную num.
num = 3
def mul():
    global num
    num = num ** 2
    return num
mul()
mul()
mul()
print(num)
'---------------------------------------------------------------'
# 7) Есть глобальная переменная, которая обозначает размер самой главной первой
# матрешки. Напишите функцию, в которой к размеру главной матрешки прибавляется
# размер второй матрешки, который определен в этой функции. То же самое сделайте и
# с третьей функцией внутри второй. Верните результат сложения.
global_size = 5

def second():
    return global_size + 3
def calculate():
    return second() + 2
result = calculate()
print(result)
'----------------------------------------------------------------'