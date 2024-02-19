#1
# peoples = {
#      "Мурат": 24,
#      "Эржан": 21,
#      "Карина": 24,
#      "Алтынай": 17,
#      "Айбек": 16
# }
# for people, age in peoples.items():
#      if age >=17:
#          print(f"{people} может пойти в ночной клуб.")
#      else:
#           print(f"{peoples} не может пойти в ночной клуб.")
        
# #2
# a = {'a': {'e': 32}, 'b': {'f': 36}, 'c': {'j': 37}, 'd': {'h': 21}}
# new_dict = {key: inner_dict[next_key] for key, inner_dict in a.items() for next_key in inner_dict}
# print(new_dict)
# #3

# fruit_prices = {'apple': 50, 'banana': 40, 'pear': 55, 'orange': 30}
# fruit_prices = {fruit: price for fruit, price in fruit_prices.items() if price % 2 != 0}
# print(fruit_prices)
# #4

# numbers_dict = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
# sum_of_values = sum(numbers_dict.values())
# print(sum_of_values)
# #5

# квадраты = {число: число ** 2 for число in range(1, 11)}

# print(квадраты)

# list_ = [-4, -3, -2, -1, 0, 1, 2, 3, 4]

# int_list = [1 if число < 0 else число for число in list_]

# print(int_list)
# #6


# my_dict = {'first': {'a': 1}, 'second': {'b': 2}}
# new_dict = {key: inner_dict[next(iter(inner_dict)) ] for key, inner_dict in my_dict.items()}
# print(new_dict)

peoples = {
     "Мурат": 24,
     "Эржан": 21,
     "Карина": 24,
     "Алтынай": 17,
     "Айбек": 16
}
for people, age in peoples.items():
     if age >=17:
         print(f"{people} может пойти в ночной клуб.")
     else:
          print(f"{peoples} не может пойти в ночной клуб.")