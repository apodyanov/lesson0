immutable_var = 1, 2, 'a', 'b', True
print(immutable_var)
# immutable_var[2] = 10 TypeError: 'tuple' object does not support item assignment, при попытке изменить кортеж система выдает ошибку, так как одной из особенностей кортежа является то, что кортеж не поддерживает обращение по элементам.

mutable_list = [1, 2, 'a', 'b', True]
print(mutable_list)
mutable_list[2] = 10
mutable_list[4] = False
print(mutable_list)