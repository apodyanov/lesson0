# Задание "Средний балл"

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
grades = [(sum([5, 3, 3, 5, 4]) / len([5, 3, 3, 5, 4])),
          (sum([2, 2, 2, 3]) / len([2, 2, 2, 3])),
          (sum([4, 5, 5, 2]) / len([4, 5, 5, 2])),
          (sum([4, 4, 3]) / len([4, 4, 3])),
          (sum([5, 5, 5, 4, 5]) / len([5, 5, 5, 4, 5]))]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaro'}
students = sorted({'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaro'})
grade_book = {students[0]: grades[0], students[1]: grades[1],
              students[2]: grades[2], students[3]: grades[3], students[4]: grades[4]}
print(grade_book)
