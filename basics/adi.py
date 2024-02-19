# num1 = int(input('Введите первое число:'))
# num2 = int(input('Введите второе число:'))
# oper = input('Введите оператора (+) (-) (*) (/):')
# if oper == '+':
#       print(num1 + num2)
# elif oper == '-':
#       print(num1 - num2)
# elif oper == '*':
#       print(num1 * num2)
# elif oper == '/':
#       print(num1 / num2)          
#       if num2 != 0:
#             print('На ноль нельзя делить')
# else:
#       print('Только (+), (-), (*)')

# count = 0
# pasww = input('Введите пароль:')
# while True:
#     print(count)        
#     if str(count) == pasww:         
#         print('Вот ващ пароль')
#         break 
#     count += 123456789000999999999    

# list_ = [20, 10, 20, 1, 100]
# min_number = None
# for i in list_:
#     if min_number is None or i <= min_number:
#         min_number = i
# print(min_number)

# lists = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# lengths = []
# for i in lists:
#     lengths.append(len(i))
# print(f'max_list {lists[max(lengths)+1]}')
# print(f'min_list {lists[min(lengths)-1]}')

# 


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