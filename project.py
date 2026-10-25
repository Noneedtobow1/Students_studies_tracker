# Ввод общих данных

num_students, num_lessons, max_rating, classwork_coefficient, selfwork_coefficient, homework_coefficient, testwork_coefficient = map(int, input("Введите через пробел: число учеников в курсе, количество занятий в курсе, максимальный рейтинг, коэффициент для активности на занятии, коэффициент для практики, коэффициент для домашней работы, коэффициент для контрольной работы: ").split())

# Проверка на правильность ввода величин

while num_students < 3:
    print("Во введённых данных ошибка")
    num_students = int(input("Введите число учеников: "))
while num_lessons <= 0:
    print("Во введённых данных ошибка")
    num_lessons = int(input("Введите число занятий: "))

while classwork_coefficient <= 0 or selfwork_coefficient <= 0 or homework_coefficient <= 0 or testwork_coefficient <= 0:
        print("Во введённых данных ошибка")
        classwork_coefficient, selfwork_coefficient, homework_coefficient, testwork_coefficient = map(int, input("Введите через пробел: коэффициент для активности на занятии, коэффициент для практики, коэффициент для домашней работы, коэффициент для контрольной работы: ").split())
        

