# Задание "Средний балл"

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
a = grades[0]
b = grades[1]
c = grades[2]
d = grades[3]
i = grades[4]
grades = [(sum(a) / len(a)), (sum(b) / len(b)), (sum(c) / len(c)), (sum(d) / len(d)), (sum(i) / len(i))]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaro'}
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaro'})
students = tuple(students) # цель данного действия закрепить отсортированные данные
                           # во избежание изменения их порядкового расположения...,
                           # пока до конца не разобрался необходимо ли это?
                           # Но программа работает как с этим действием, так и без него.
# print(type(students))
# print(students)
grade_book = {students[0]: grades[0], students[1]: grades[1],
              students[2]: grades[2], students[3]: grades[3], students[4]: grades[4]}
# print(grade_book['Steve'])
print(grade_book)
