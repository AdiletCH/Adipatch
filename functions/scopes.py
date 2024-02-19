'========================Область видимости======================='
#LEGB - local enclosed global build-in

'========================Build-in====================='
# встроенное пространство имен (list, print, dict, len, input)

'==========================Global====================='
# все переменные, которые мы создали внутри файла
# чтобы посмотреть все глобальные переменные, можно использовать функцию globals
a = 10
b = 'hello'
print(globals())

'==========================enclosed==================================='
#замкнутым пространство имен - это локальное пространство, у которого есть внутреннее локальное пространство

var = 'global' # хранится глобальном пространство

def func():
    var = 'enclosed' # замкнутое пространство
    def inner_func():
        var = 'local'
        print(var) # local
    print(var) ## enclosed
    inner_func()
print(var) # global
func()

'====================Local===================='
# локальное пространство имён - это пространство которое находится внутри функции

a = 10
def func(a, b):
    res = a + b
    print(res)
    print(locals())

func(10, 5)


def count_(num):
    count = 0
    def inner_count_():
        nonlocal count
        count+=1
        print(count)
    for i in range(num):
        inner_count_()


count_(10, 98)


