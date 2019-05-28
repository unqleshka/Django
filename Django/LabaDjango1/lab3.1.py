#coding:utf-8
groupmates = [
    {
        "name": u"Василий",
        "group": "БСТ1701",
        "age": 19,
        "marks": [4, 3, 5, 5, 4]
    },
    {
        "name": u"Анна",
        "group": "БСТ1701",
        "age": 21,
        "marks": [3, 2, 3, 4, 3]
    },
    {
        "name": u"Георгий",
        "group": "БСТ1702",
        "age": 20,
        "marks": [3, 5, 4, 3, 5]
    },
    {
        "name": u"Максим",
        "group": "БСТ1703",
        "age": 19,
        "marks": [5, 5, 5, 4, 5]
    }
]

def print_students(students):
    print (u"Имя студента".ljust(15), u"Группа".ljust(8), \
        u"Возраст".ljust(8), \
        u"Оценки".ljust(20))
    for student in students:
        print (student["name"].ljust(15), \
            student["group"].ljust(8), \
            str(student["age"]).ljust(8), \
            str(student["marks"]).ljust(20))
    print ("\n")

print_students(groupmates)
ave = float(input("Введите среднюю оценку студента: "))
average = []
for student in groupmates:
    if float(sum(student["marks"])) / len(student["marks"]) >= ave:
        average.append(student)
print_students(average)
input("\nНажмите Enter для выхода из програмы\n")