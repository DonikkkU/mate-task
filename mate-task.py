#mate_1
set1 = {10, 20, 30, 40, 50}
set1.difference_update({10, 20, 30})
print(set1)
#mate_2
set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 20, 10}
a = list(set1)
b = list(set2)
c = []
for i in a:
    for j in b:
        if i == j:
            c.append(i)
            break
print(sum(c))
#mate_#3
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
print(set1 - set1.symmetric_difference(set2))
#mate_4
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

set1.symmetric_difference_update(set2)
print(set1)
#mate_dict_1

key_list = ['Ten', 'Twenty', 'Thirty']
values_list = [10, 20, 30]
dictionary = dict(zip(key_list, values_list))
print(dictionary)

#students_list
students = {
    'name': [],
    'age': [],
    'id': []
}
choice = 1
while choice != 0:
    print('0- завершить программу')
    print('1- зарегестрировать студента')
    print('2- удалить студента из сприска')
    print('3- получить список студентов')
    choice = int(input('выполнить действие:'))
    if choice == 1:
        n = (input('Зарегестрировать студента:'))
        a = int(input('Введите возраст студента:'))
        b = int(input('id:'))
        students['name'].append(n)
        students['age'].append(a)
        students['id'].append(b)
        print(students)
    elif choice == 2:
        delete = input('Введите имя студента которого хотите удалить:')
        my_index = students['name'].index(delete)
        del students['name'][my_index]
        del students['age'][my_index]
        del students['id'][my_index]
        print(students)
    elif choice == 3:
        for i in students:
            print('\n'.join("{}: {}".format(k, v) for k, v in students.items()))
            print('\n')
    elif choice == 0:
        print(('Программа завершена. Продуктивного вам дня'))
    else:
        print('Invalid coice!')
