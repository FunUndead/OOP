
# подсчёт средней оценки за ДЗ по всем студентам
def average_rating(list, course):
    list_all = []
    for x in list:
       for subject, v in x.grades.items():
           if course == subject:
            rating = sum(v) / len(v)
            list_all += [rating]
    rating_all = sum(list_all) / len(list)
    return print(rating_all)

class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}

# сравнение по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Student):
            print('Один из них не студент!')
        for subject, v in self.grades.items():
            rating_1 = sum(v) / len(v)

        for subject_2, v in other.grades.items():
            rating_2 = sum(v) / len(v)

        return rating_1 < rating_2

# перезагрузка
    def __str__(self):
        for subject, v in self.grades.items():
            average_rating = sum(v) / len(v)

        cours_finish = ','.join(self.finished_courses)
        cours = ', '.join(self.courses_in_progress)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за домашнее задание: {average_rating}\
        \nКурсы в процессе изучения: {cours}\nЗавершенные курсы: {cours_finish}\n"

# выставление оценки лектору
    def rate_lec(self, lecturer, course, grade):
        if isinstance(lecturer, Lecturer) and course in lecturer.courses_attached and course in self.courses_in_progress:
            if course in lecturer.grades:
                lecturer.grades[course] += [grade]
            else:
                lecturer.grades[course] = [grade]
        else:
            return 'Ошибка'

class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer (Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = {}
        self.courses_attached = []

# перезагрузка
    def __str__(self):
        for subject, v in self.grades.items():
            average_rating = sum(v) / len(v)
        return f"Имя: {self.name}\nФамилия: {self.surname}\nСредняя оценка за лекцию: {average_rating}\n"

# сравнение двух лекторов по средней оценке
    def __lt__(self, other):
        if not isinstance(other, Lecturer):
            print('Один из них не лектор!')
        for subject, v in self.grades.items():
            average_rating = sum(v) / len(v)

        for subject_2, v in other.grades.items():
            average_rating_2 = sum(v) / len(v)
        return average_rating < average_rating_2

class Reviewer (Mentor):

# выставление оценки студенту
    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Ошибка'

# перезагрузка
    def __str__(self):
        return f"Имя: {self.name}\nФамилия: {self.surname}\n"

# создание студента 1
best_student = Student('Ruoy', 'Eman', 'your_gender')
best_student.courses_in_progress += ['Python']
best_student.courses_in_progress += ['Git']
best_student.finished_courses += ['Введение в программирование']

# создание студента 2
best_2_student = Student('Fred', 'White', 'your_gender')
best_2_student.courses_in_progress += ['Python']
best_2_student.courses_in_progress += ['Git']
best_2_student.finished_courses += ['Введение в программирование']

# создание reviewer 1
cool_reviewer = Reviewer('Some', 'Buddy')
cool_reviewer.courses_attached += ['Python']

# создание reviewer 2
cool_reviewer_2 = Reviewer('Bred', 'Pitt')
cool_reviewer_2.courses_attached += ['Python']

# выставление оценок студенту 1
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)
cool_reviewer.rate_hw(best_student, 'Python', 10)


# выставление оценок студенту 2
cool_reviewer.rate_hw(best_2_student, 'Python', 10)
cool_reviewer.rate_hw(best_2_student, 'Python', 10)
cool_reviewer.rate_hw(best_2_student, 'Python', 10)

# создание лектора 1
cool_lecturer = Lecturer('Alex', 'Fish')
cool_lecturer.courses_attached += ['Python']

# создание лектора 2
cool_lecturer_2 = Lecturer('Masha', 'Black')
cool_lecturer_2.courses_attached += ['Python']

# выставление оценки за лекцию
best_student.rate_lec(cool_lecturer, 'Python', 8)
best_student.rate_lec(cool_lecturer, 'Python', 9)

best_student.rate_lec(cool_lecturer_2, 'Python', 8)
best_student.rate_lec(cool_lecturer_2, 'Python', 7)

# вывод оценок студента
print(best_student.grades)
# вывод оценок лектора
print(cool_lecturer.grades)

print(cool_reviewer)

print(cool_lecturer)
print(best_student)

# сравнение студентов
print(best_student > best_2_student)
# сравнение лекторов
print(cool_lecturer > cool_lecturer_2)

# список студентов
students_list = [best_2_student, best_student]
# список лекторов
lecturer_list = [cool_lecturer_2, cool_lecturer_2]

# средняя оценка по предмету студентов
result = average_rating(students_list, 'Python')

# средняя оценка за лекцию лекторов
result_2 = average_rating(lecturer_list, 'Python')






