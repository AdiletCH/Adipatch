'+++++++++++++++++++++++++++++STRING++++++++++++++++++++++++++++++++'
#Строки - это неизменяемый тип данных, который предназначен для хранения текстов, 
#заключенного в одинарные или двойные кавычки

string1 = 'строка c одинарными ковычками'
string2 = "стркоа с двойными ковычками"
# string3 = 'неправильная строка"
string4 = " Don't " #внутри двойной ковычки одинарная, воспринимает как ковычку как часть текста
string5 = '''Многострочный текст в одинарных/двойных кавычках, тут можно ставить "любые" кавычки'''
string6 = 'hello' + 'world' #контатинация (плюс между слов)
# print (string6)

# string7 = 'А ' * 8 #умножение на число (АААААААА)
# print (string7)


'+++++++++++++++++++++++++++++ЭКРАНИЗАЦИЯ СТРОК+++++++++++++++++++++++++'
'\n'#перенос текста на новую строку
# print('hello\nworld')
#hello
#world

'\t'#табуляция
# print('kakadu\tkoala')

str1 = 'don\'t' #отображает кавычку ' в терминале (воспринимает ее как текст)
# print(str1)
str2 = "don\"t"
# print(str2)

str3 ='символ - \\'
# print (str3)

'\v'#перенос на новую строку со смещением вправо на длину предыдущей строки
str4 = 'sdfafasd\vclown\vsdfasd\vsdadga'
# print (str4)

'\r'#перенос каретки на начало строки
str5 = 'makers bootcamp\rHI'
print (str5)
# HIkers bootcamp


'===============Форматирование строк=============='
#1
title = 'iphone14'
price = 150
format_1 = 'Мой телефон', title, 'стоит', price, 'долларов'
format_2 = f'Мой телефон {title} стоить {price} $'

print(format_2)

#2
string = 'Название : {} Цена: {}'
print(string.format('iPhone', 150))

#3 
string = 'Название: %s Цена: %s'
print(string % ('iPhone', 150))

'==============Методы строк============'
# методы - функции, которые относятся к определенному классу, к ним можно обращаться через точки

print(dir(str))

string = 'hello'

print(string.upper()) #makers -> MAKERS
print(string.lower()) #MAKERS -> makers
print(string.swapcase()) #MaKErS mAkeRs


print(string.title()) # hello world -> Hello World
print(string.capitalize()) # hello world -> Hello world
print(string.center(11, '-')) # '   hello   '

print(string.count('l')) # hello -> 2

string = 'hello'
print(string.startswith('a')) #False
print(string.startswith('h')) #True
print(string.startswith('H')) #False
print(string.endswith('d')) #False
print(string.endswith('llo')) #True

string = 'makers'
print(string.islower()) # makers -> True
print(string.isupper()) # MAKERS -> True

string = '1235243'
print(string.isdigit()) #True - проверка на цифры в тексте
print(string.isalpha()) #False - проверка на буквы в тексте
string = 'makers1234556'
print(string.isalnum()) # True - проверка на то что является ли строка с числами или с буквами или все вместе, но не символы

string = 'hello world makers bootcamp'
print(string.split()) 



'========================Индексы===================='
# индекс - порядковый номер элемента в последовательности (символа в строке), (индексация начинается с 0)

'h e l l o  w o r l d'
#0 1 2 3 4 5 6 7 8 9 10
#             -3 -2 -1

string = 'hello world'
print(string[0]) # 'h'
print(string[7]) # 'o'
print(string[10]) # 'd'
print(string[-1]) # 'd'

#срезы - подстрока (часть строки)
#string[start:end(не включительно):step]
string = 'hello world'
print(string[3:8]) # 'lo wo'
print(string[:]) #'hello world'
print(string[6:]) #'world'
print(string[:5]) #'hello'

string = 'hello world'
print(string[::-1]) # 'dlrow olleh'
print(string[::2]) # hlowrd
print(string[::3]) # hlwl
print(string[::4]) #hor

string = 'hello'
string.upper() # hello -> HELLO
print(string)