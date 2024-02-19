'=====================Функция===================='
# функия - это именнованный блок кода, который может принимать аргументы и возвращать результат

# def get_sum(x, y): # x, y - параметры
#     result = x + y
#     return result

# print(get_sum(10, 20))

# a = 10 # 10, 20 - аргументы

"Функции соблюдают принцип DRY (don't repeat yourself)"
'==========================Аргументы и параметры=========================='

# параметры - переменные внутри функции, задаются при создании функции

# аргументы - значения, которые мы передаем при вызове функции

'================================Виды параметров======================================='
#1. обязательные
#2. не обязательные
#    1. с дефолтом(со значением по умолчанию)
#    2. args(все позиционные аргументы)
#    3. kwargs(все лишние именнованные аргумент)

# def func(*args):
#     print(args)

# print(func(1,2,3, 'hi'))

'========================================Виды аргументов============================================='
#1.позиционные (по позиции)
#2. именнованные (по названию (параметр = значение))

def func(a,b,c,d):
    ...
func(d= 5, c =3, a = 1, b = 0)
'----------------------------------------------------'
# num : int = 10
# name : str = 'makers'

# def sum_(a:int, b:int):
#     return a + b

# print(sum_(13, 10))


def calc_():
    try:
        num1 = float(input('Enter number: '))
        num2 = float(input('Enter number2: '))
        oper = input('Enter oper: ')
        if oper == '+':
            print(num1+num2)
        elif oper == '-':
            print(num1-num2)
        elif oper == '/':
            print(num1/num2)
        elif oper == '*':
            print(num1*num2)
        elif oper == '**':
            print(num1**num2)
        else:
            raise KeyError
    except KeyError:
        print('Вы вели не ту операцию')      
    except ZeroDivisionError:
        print('На ноль нельзя делить')
    except ValueError:
        print('Введите число, а не символы')

calc_()      
'------------------------------------------------'



db = [
    {'name':'Tima', 'password':hash('123456789')},
    {'name':'Nick', 'password':hash('123456')}
]

def in_database(name):
    for user in db:
        if name == user['name']:
            return True
    return False    

def register(name, password, password2):
    if in_database(name):
        raise Exception('Юзер с таким именем уже существует')
    if password != password2:
        raise Exception('Пароли не совподают')
    user = {'name':name, 'password':hash(password)}
    db.append(user)
    return 'Вы успешно зарегестрировались'

def login(name, password):
    if not in_database(name):
        raise Exception('Пользователь не найден!')
    for user in db:
        if user['name'] == name:
            if user['password'] != hash(password):
                raise Exception('Пароль не верный!')
    return 'Вы успешно залогинились'

print(register('katana', '123123123', '123123123'))        
print(db)
print(login('katana', '123123123'))

'======================Lambda======================='
# lambda - анонимная функция, которая записывает в одну строчку

# def sum_1(x,y):
#     return x + y

# sum_2 = lambda x, y: x + y







