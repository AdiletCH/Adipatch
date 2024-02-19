'================Словари==============='
# dick - изменяемый, интерируемый, неупорядоченный, неиндексируемый тип данных, для хранения данных в парах(ключ:значение)

user = {'name':'sultan', 'age':20, 'nick':'katana'}

print(user['age']) #20
print(user['nick']) # katana
print(user['name']) # sultan

# {ключ:значение, ключ:значение...}
#ключ - не изменяемый тип данных, уникальный(если ключ повторяется, то сохранится тот, который яыляется последним)
#значение - любые: и изменяемый, и неизменяемый тип данных. Могут повторяться

'====================Создание====================='
dick1 = {'a':1, 'b':2}
dick2 = dict([('a',1),('b',2)])
dick3 = dict(['a1','b2'])
dick4 = {}
dick4['name'] = 'tima'
dick4['age'] = 100
dick4['nick'] = 'collection'
print(dick4)

'===================Методы словарей===================='
# get - метод, который возвращает значение по ключу, если такого ключа нет то возвращает дефолтное значение, чаще всего None
user = {
    'name':'Nick',
    'age': 100,
    'telephon_number':'+1234567'
}
#print(user['nafufj']) # KeyError
print(user.get('age', 'Нет такого ключа')) #100
print(user.get('name')) #Nick
print(user.get('id')) #None

#pop - удаляет пару по ключу и возвращаеь значение
dict_ = {'a':1, 'b':2, 'c':3}
popped_values = dict_.pop('a')
print(popped_values) # 1
print(dict_) # {'b':2, 'c':3}

#popitem - удаляет последнюю пару и возвращает ее

dict_ = {'a':1, 'b':2, 'c':3}
popped_values = dict_.popitem()
print(popped_values) # ('c':3)

#print(dir(dict))

# update - расширяет словарь парами из второго словаря

dict1 = {1: 'a',2:'b'}
dict2 = {2:'c',4:'d'}
dict1.update(dict2)
print(dict1) # {1:'a', 2:'c',4:'d'}

# clear - очищает словарь
dict_ = {1:1, 2:2, 3:3}
dict_.clear()
print(dict_) # {}

# fromkeys - метод создания нового словаря, используя список ключей

dict_ = dict.fromkeys([1,2,3], True) #{1: True, 2: True, 3: True}
print(dict_)

dict2 = dict.fromkeys('abcd', 0)
print(dict2) #{'a': 0, 'b': 0, 'c': 0, 'd': 0}

# list.copy(), list.deepcopy()
# dict.setdefault()

# items - метод, который достает ((ключ, значение),(ключ значение)...)
# keys - метод который возвращает ключиъ
#values - метод который возвращает значения
dict_ = {'a':1, 'b':2, 'c':3}
print(dict_.values())
print(dict_.keys())
print(dict_.items())

'=================================Циклы с dict======================================'
dict_ = {'a':1, 'b':2, 'c':3}

# print(dict_['a'])
# print(dict_['b'])
# print(dict_['c'])

for i in dict_:
    print(i)

# dick_ = {'a':1, 'b':2, 'c':3}

dick_2 = {}
for k, v in dict_.items():
    dick_2[v] = k
print(dick_2)    




















