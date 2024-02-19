'====================Встроенные функции========================'
# map, filter, reduce, zip, enumerate

'ZIP'
# соединеяет несколько последовательностей (получаем генератор, в котором элементы - tuple) (zip object)

list_1 = [1, 2, 3, 4]
list_2 = ['a', 'b', 'c']
list_3 = [10.5, 20.0, 1.3, 0.5]

zipped = zip(list_1, list_2, list_3)
print(zipped) # <zip object at zip object at 0x7f7518087bc0>
print(list(zipped)) # [(1, 'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3)]
print(tuple(zipped)) # ((1, 'a', 10.5), (2, 'b', 20.0), (3, 'c', 1.3))
print(dict(zipped)) # будет работать только с двумя листами в zip()

'ENUMERATE'
# нумерует последовательность (по дефолту с 0), (тоже возвращает генератор)
# <enumerate object 0x7f7518087bc0>

enumerated = enumerate('hello world') 
print(enumerated)# <enumerate object 0x7f7518087bc0>
# print(list(enumerated)) # [(0, 'h'), (1, 'e'), (2, 'l'), (3, 'l'), (4, 'o'), (5, ' '), (6, 'w'), (7, 'o'), (8, 'r'), (9, 'l'), (10, 'd')]
for elem in enumerated:
    print(elem)

'MAP'
# принимает функцию и последовательность
# записывает в новую последовательность результат функции принимив каждый элемент последовательность
# <map object 0x7f7518087bc0>
list_ = ['1', '2', '3', '4']       
mapped = map(int, list_) # <map object 0x7f7518087bc0>
print(list(mapped)) #[1, 2, 3, 4]

mapped2 = map(str.isdigit, list_)
print(list(mapped2))

list_ = [12, 34, 1, 2, 6]
def pow_(x):
    return x ** 2

print(list(map(pow_, list_)))

print(list(map(lambda x:x**2, list_)))

str_ = 'hello world'
mbappe = map(str.upper, str_)
print(''.join(list(mbappe)))

print(''.join(list(map(str.upper, 'hello world'))))

'FILTER'
# возвращает генератор с элементами прошедшими фультрацию (какое-то условие), принимает функцию и последовательность
# filter object 0x7jgfjfgk37f29

list_ = [12, -23, 0, -1, -34, 38]
filtered = filter(lambda x: x >= 0, list_)
print(list(filtered))

users = [
    {'name':'makers', 'age':20},
    {'name':'anonym', 'age':15},
    {'name':'sem', 'age':25}
]
filtered = filter(lambda x: x['age'] > 18, users)
print(list(filtered))

'REDUCE'
# принимает функцию и последовательность, но возвращает 1 элемент (передаваемая функция должна приниимать 2 аргумента)
# импортируется из functools

from functools import reduce

list_ = [1,5,4,1,5,5]
res = reduce(lambda x, y: x * y, list_)
print(res)

users = [
    {'name':'makers', 'age':20},
    {'name':'anonym', 'age':15},
    {'name':'sem', 'age':25}
]

def func(x, y):
    if x['age'] < y['age']:
        return x
    else:
        return y
    
print(reduce(func, users))

list_ = [1,2,3,4,5,6,1,9,-6,-12]
res = reduce(lambda x, y: x if x<y else y, list_)
print(res)
