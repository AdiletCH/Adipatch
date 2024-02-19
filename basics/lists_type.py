'===============Методы строчек================'
# list_.append(True)
# list_.append('text')
# list_.append(123)
# list_.append([1,2,3])
# print(list_) #

#pop - удаляет элемент из списка по индексу и возвращает удаленный элемент, если не передать индекс в скобки то удаляет последний элемент

list_ = [51,'hi',True,123,'q',12,0]
rm_elem = list_.pop(3)
print(rm_elem) # 123
print(list_) #[51,'hi',True,'q',12,0]

# remove - удаление элемента из списка по значению

list_ = [12, 'makers', 234, True, 0, 1, 1, 1]
list_.remove('makers')
print(list_)

'---------------------------------------------------------------'
# count - метод, который считает кол-во элементов в списке

list_ =[0, 12, 'hi', True, False, True, 0, 1, 1, 0]
count_of_elem = list_.count(1)
print(count_of_elem) #4

'---------------------------------'

#index - возвращает индекс первого вхождения указанного элемента

list_ = [12, 1, 1, 1, 'hi', None]
index_ = list_.index('hi')
print(index_) #4

'---------------------------------------------'
#insert - добавляет эелемент в список по указаннному индексу 

list_ = [1, 2, 3, 'hi', 5, 1,True, 'world']
list_.insert(4, 'makers')
print(list_)

'-----------------------------------------'
#extend - добавляет элементы списка в другой список
list1 = [0,0,0]
list2 = [1,2,3]
list1.append(list2) # [0,0,0,[1,2,3]]
list1.extend(list2) # [0,0,0, 1,2,3]
print(list1)
'-------------------------------------'


#reverse - расставляет элементы в обратном порядке
list_ = [1,2,3,4, None, [1,2,3]]
list_.reverse()
print(list_) # [[1,2,3], None, 4,3,2,1]

# sort = сортирует список состоящий из эелементов одного типа данных
list_ = [23, 1, 24, 23, 123, 0]
list_.sort()
print(list_) #b[0, 1, 23, 23, 24, 123]

list_ = ['hi', 'makers', 'hello', 'world']
list_.sort(key=len, reverse=True)
print(list_) # ['makers', 'hello', 'world', 'hi']

'==========================Tuple============================='
#кортеж - упорядоченный, неизменяемый, итерируемый тип данных, литералы (,)
tuple_ = (1,2,3,True, False, None, 'hi')
print(dir(tuple))

# есть тольком2 метода это - index и count 

a = 15
a, b, c = 15, 5, 'hi'
print(a)

