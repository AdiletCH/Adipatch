'======================Compretehensions======================'
#генератор, с помощью которого мы можете создавать последовательности используя цикл for в одну строку

# элемент for элемент in последовательность
# елемент for елемент in последовательность if фильтр
# елемент if условие1 else елемент2 for елемент in последовательность

compr_ = [i for i in range(10) if i % 2 ==0]
print(compr_)

compr_1 = []
for i in range(6):
    if i % 2 == 0:
        compr_1.append(i)
print(compr_1)    

list_ = [12, None, 'hi', 123, 1, 6, 2, True, 0, False]

new_list_ = [i for i in list_ if bool(i)]
print(new_list_)

new_list_2 = [i if bool(i) else 0 for i in list_]
print(new_list_2)

new_list_2 = []
for i in list_:
    if bool(i):
        new_list_2.append(i)
    else:
        new_list_2.append(0)


list_ = [12, 3, 0, 34, 9, 7]
new_list_ = ['четное' if i % 2 == 0 else 'нечетное' for i in list_]
print(new_list_)



list_ = [1, 'hi', 123, 'hello world', True, 'makers', False]

new_list_2 = []
for i in list_:
    if type(i) == str:
        new_list_2.append(i)
print(new_list_2)

'=================Виды comprehenshion=================='

# list comprehension -> []
# dict comprehension -> {:}
# set comprehension -> {}

# comprehension генератор -> ()

'DICL COMPREHENSION'
# {1:1, 2:4, 3:9, 4:16}

dict_ = {i:i**2 for i in range(1,5)}
print(dict_)
'-------------------------------'
dict_ = {'a':1, 'b':2, 'c':3}
new_dict_ = {v:k for k,v in dict_.items()} # {1:'a', 2:'b', 3:'c'}
print(new_dict_)
'-----------------------------'
new_dict_2 = {v**2:v for v in dict_.values() if v % 2 == 0}
print(new_dict_2)



'SET_COMPREHENSION'
set_ = {i for i in range(11) if i % 2 == 0}
print(set_)

set_1 = {12, 34,1, 'hi', 'hello', 123, None}
set2 = {i for i in set_1 if type(1)==str}
print(set2)

'========================Вложеные comprehension========================'

# Создайте словарь, где ключами будут числа от 1 до 5, а значениями - списки с числами от 1 до этого числа

# 

dict_ = {}
for i in range(1,6):
    key = i 
    values = [j for j in range(1, i+1)] 
    dict_[key] = values

dict_ = {i: [j for j in range(1, i+1)] for i in range(1,6)} 

print(dict_)

