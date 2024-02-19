'=====================Фунция высшего порядка==================='
# функция высшего порядка - это функция которая принимает в аргументы другую функцию, создает внутри себя другую функцию, вызывае  фунуцию и возвращает функцию

def func1():
    return 'hi'

def func2(func_):
    print(func_())    

func2(func1)   

'================Декораторы==============='
# декораторы - это функция высшего порядка, которая нужна для расширения функционала другой функции не изменяя ее (функция оберток)

def decorator_glushitel(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        res = 'тихо' + text   
        print(res)
    return wrapper 

def gun():
    return('стрелять')  

decorator_glushitel(gun)  

'----------------------------------------'
def decorator_glushitel(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        res = 'тихо' + text   
        print(res)
    return wrapper 

@decorator_glushitel
def gun():
    return('стрелять')  

gun() # способ использовать декоратор при помощи синтаксического сахара

'------------------------------------'
from datetime import datetime

def decorator(func):
    def wrapper():
        print('start:', datetime.now())
        func()
        print('finish:', datetime.now())
    return wrapper

@decorator
def hello():
    print('hello world')

hello()    
'--------------------------------------'
def func_start_time(func):
    def wrapper(*args, **kwargs):
        print('start:', datetime.now())
        func(*args, **kwargs)   
    return wrapper

@func_start_time
def sum_(a, b):
    print(a + b)   

sum_(20, 10)    
'----------------------------------------'
def decorator(num):
    def inner_decorator(func):
        def wrapper(*args, **kwargs):
            for i in range(num):
               func(*args, **kwargs)
        return wrapper
    return inner_decorator    

@decorator(10)
def hello():
    print('hello world')

hello()    
'----------------------------------------'
def call_function(func):
    def wrapper(*args, **kwargs):
        print('Вызываю функции', func.__name__)
        func(*args, **kwargs)
        print('Вызов функции', func.__name__, 'прошел успешно')
    return wrapper


@call_function
def first():
    print("hello world")
    return "hello world"
first()