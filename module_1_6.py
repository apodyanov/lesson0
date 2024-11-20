# Работа со словарями:
my_dict = {'Max': 1993, 'Andrey': 1956, 'Dima': 2009}
print(my_dict)
print(my_dict['Andrey'])
print(my_dict.get('Eva', 'Такой ключ отсутствует в словаре'))
my_dict.update({'Eva': 2005, 'Vika': 2011})
print(my_dict)
a = my_dict.pop('Dima')
print(a)
print(my_dict)

# Работа с множествами:
my_set = {1, 1, 2, 2, 'множество', 55, 66, 55, True, 66, 'множество', ('apple', 2024, 'orange'), True, ('apple', 2024, 'orange')}
print(my_set)
my_set.add('множество1')
my_set.add(2025)
my_set.remove('множество')
print(my_set)