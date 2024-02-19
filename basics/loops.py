'===================Циклы==================='
# циклы - это блок кода, который отрабатывает несколько раз 

'итерируемый объект - это какая-та последовательность, которую мы можем перебрать. Например: [1,2,3], - list, "hello world" - str, {"a":1, "b":2} - dict, (1,2,3,4,123,True) - tuple '
"""Итерация - процесс перебора итерируемого объекта"""


# 1. for - цикл, который работает с итерируемым объектом, цикл заканчивает свою работу, когда он доходит до последнего элемента итерируемого объекта

# 2. while - цикл, который работает до тех пор пока условия верное 

'FOR'
# list_ = [1, True, 'hello', 0, 123]
# for elem in list_:
#     if elem != 0:
#         print(elem)

'WHILE'

count = 0
while count <= 10:#True
    print(count) 
    count = count + 2

'====================Ключевые слова в циклах===================='
# break - оператор, который останавливает работу цикла (ломает)
# continue - оператор, который пропускает итерацию (продолжает с другой итерации)

# range (start, end, step) - генератор последовательности, от start до end (не включительно)

print(list(range(1234567, 1, -500)))
'---------------------------------------------------------------------'
for i in range(0, 21):
    if i == 10:
        continue
    print(i)

for i in ('1','2','3' 'world', '12'):
    if i.isdigit():
        print(int(i)) # '1' -> 1, '2' -> 2, '3' -> 3, Error
        print('Все прошло хорошо!')
    elif i.isalpha():
        print('Я не могу перевести буквы число')    
        break    
    else:        
        print('Я нвешл символы!')

count = 0
pasww = input('Введите пароль:')
while True:
    print(count)        
    if str(count) == pasww:         
        print('Вот ващ пароль')
        break 
    count += 1 #count = count + 1

# count = 0    
# while True:
#     if 1 != 0:
#         continue
#     if count == 1:
#         break
#     print(count)    
#     count +=1
# else:

#else в цикле работает тогда когда условие цикла стонавится false, если же сработал brake, то else не работает
            
