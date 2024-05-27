from sqlalchemy import create_engine, MetaData
from sqlalchemy import func
from sqlalchemy.orm import sessionmaker
import json

with open("config.json", "r") as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/academy'
engine = create_engine(db_url)

metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

departments = metadata.tables['departments']
faculties = metadata.tables['faculties']
groups = metadata.tables['groups']
teachers = metadata.tables['teachers']
curators = metadata.tables['curators']
subjects = metadata.tables['subjects']
groups_lectures = metadata.tables['groups_lectures']
lectures = metadata.tables['lectures']
groups_curators = metadata.tables['groups_curators']


# вивести інформацію про всі навчальні групи
def report_groups_info():
    result = session.query(groups.c.name, groups.c.rating, groups.c.year, departments.c.name.label("department_name")) \
        .join(departments, groups.c.department_id == departments.c.id).all()

    if result:
        for row in result:
            group_info = ' '.join(map(str, row))
            print(group_info)


# вивести інформацію про всіх викладачів
def report_teachers_info():
    result = session.query(teachers).all()
    if result:
        for row in result:
            teacher_info = ' '.join(map(str, row))
            print(teacher_info)


# вивести назви усіх кафедр
def report_departments_names():
    result = session.query(departments.c.name).all()

    if result:
        for row in result:
            print(f"{row.name}")


# вивести імена та прізвища викладачів, які читають лекції в конкретній групі
def report_group_teachers():
    group_name = input("Enter the group name: ")
    result = session.query(teachers.c.surname, teachers.c.name) \
        .join(lectures, lectures.c.teacher_id == teachers.c.id) \
        .join(groups_lectures, groups_lectures.c.lecture_id == lectures.c.id) \
        .join(groups, groups_lectures.c.group_id == groups.c.id) \
        .filter(groups.c.name == group_name).all()

    if result:
        for row in result:
            print(f"{row.surname} {row.name}")


# вивести назви кафедр і груп, які до них відносяться
def report_department_groups():
    result = session.query(departments.c.name.label("department_name"), groups.c.name.label("group_name")) \
        .join(groups, groups.c.department_id == departments.c.id).all()
    if result:
        for row in result:
            print(f"{row.department_name} {row.group_name}")


# 6. відобразити кафедру з максимальною кількістю груп
def report_max_groups_department():
    sub_result = session.query(departments.c.name.label("department_name"),
                               func.count(groups.c.id).label("group_count")) \
        .join(groups, groups.c.department_id == departments.c.id).group_by(departments.c.name).all()
    if sub_result:
        max_count = max(count[1] for count in sub_result)
        max_departments = [row[0] for row in sub_result if row[1] == max_count]
        for department_name in max_departments:
            print(department_name)


# 7. відобразити кафедру з мінімальною кількістю груп
def report_min_groups_department():
    sub_result = session.query(departments.c.name.label("department_name"),
                               func.count(groups.c.id).label("group_count")) \
        .join(groups, groups.c.department_id == departments.c.id).group_by(departments.c.name).all()
    if sub_result:
        min_count = min(count[1] for count in sub_result)
        min_departments = [row[0] for row in sub_result if row[1] == min_count]
        for department_name in min_departments:
            print(department_name)


# 8. вивести назви предметів, які викладає конкретний викладач
def report_teacher_subjects():
    teacher_surname = input("Enter the teacher surname: ")
    teacher_name = input("Enter the teacher name: ")
    result = session.query(subjects.c.name) \
        .join(lectures, lectures.c.subject_id == subjects.c.id) \
        .join(teachers, lectures.c.teacher_id == teachers.c.id) \
        .filter(teachers.c.surname == teacher_surname, teachers.c.name == teacher_name).all()

    if result:
        for row in result:
            print(f"{row.name}")


# 9. вивести назви кафедр, на яких викладається конкретна дисципліна
def report_subject_departments():
    subject_name = input("Enter the subject name: ")
    result = session.query(departments.c.name) \
        .join(groups, groups.c.department_id == departments.c.id) \
        .join(groups_lectures, groups_lectures.c.group_id == groups.c.id) \
        .join(lectures, lectures.c.id == groups_lectures.c.lecture_id) \
        .join(subjects, lectures.c.subject_id == subjects.c.id) \
        .filter(subjects.c.name == subject_name).all()

    if result:
        for row in result:
            print(f"{row.name}")


# 10. вивести назви груп, що належать до конкретного факультету
def report_faculty_groups():
    faculty_name = input("Enter the faculty name: ")
    result = session.query(groups.c.name.label("group_name")) \
        .join(departments, groups.c.department_id == departments.c.id) \
        .join(faculties, faculties.c.id == departments.c.faculty_id) \
        .filter(faculties.c.name == faculty_name).all()
    if result:
        for row in result:
            print(f"{row.group_name}")


# 11. вивести назви предметів та повні імена викладачів, які читають найбільшу кількість лекцій з них
def report_teachers_max_subject_lectures():
    lecture_counts = session.query(teachers.c.surname, teachers.c.name, subjects.c.name.label("subject_name"),
                                   func.count(lectures.c.id).label("lecture_count")) \
        .join(lectures, lectures.c.teacher_id == teachers.c.id) \
        .join(subjects, subjects.c.id == lectures.c.subject_id) \
        .group_by(teachers.c.surname, teachers.c.name, subjects.c.name).subquery()

    max_lecture_counts = session.query(lecture_counts.c.subject_name,
                                       func.max(lecture_counts.c.lecture_count).label("max_lecture_count")) \
        .group_by(lecture_counts.c.subject_name).subquery()
    max_lectures_query = session.query(lecture_counts.c.surname, lecture_counts.c.name,
                                       lecture_counts.c.subject_name) \
        .join(max_lecture_counts,
              (lecture_counts.c.subject_name == max_lecture_counts.c.subject_name) &
              (lecture_counts.c.lecture_count == max_lecture_counts.c.max_lecture_count)).all()
    for row in max_lectures_query:
        print(f'{row.surname} {row.name} {row.subject_name}')


# 12. вивести назву предмету, за яким читається найменше лекцій
def report_subjects_with_min_lectures_count():
    lectures_count = session.query(subjects.c.name, func.count(lectures.c.id).label("lectures_count")) \
        .join(lectures, lectures.c.subject_id == subjects.c.id) \
        .group_by(subjects.c.name).subquery()
    min_lectures_subject = session.query(func.min(lectures_count.c.lectures_count).label("min_lectures_count")).scalar()
    result = session.query(lectures_count.c.name) \
        .filter(lectures_count.c.lectures_count == min_lectures_subject).all()
    for row in result:
        print(f'{row.name}')


# 13. вивести назву предмету, за яким читається найбільше лекцій
def report_subjects_with_max_lectures_count():
    lectures_count = session.query(subjects.c.name, func.count(lectures.c.id).label("lectures_count")) \
        .join(lectures, lectures.c.subject_id == subjects.c.id) \
        .group_by(subjects.c.name).subquery()
    max_lectures_subject = session.query(func.max(lectures_count.c.lectures_count).label("min_lectures_count")).scalar()
    result = session.query(lectures_count.c.name) \
        .filter(lectures_count.c.lectures_count == max_lectures_subject).all()
    for row in result:
        print(f'{row.name}')


while True:

    print("1. вивести інформацію про всі навчальні групи")
    print("2. вивести інформацію про всіх викладачів")
    print("3. вивести назви усіх кафедр")
    print("4. вивести імена та прізвища викладачів, які читають лекції в конкретній групі")
    print("5. вивести назви кафедр і груп, які до них відносяться")
    print("6. відобразити кафедру з максимальною кількістю груп")
    print("7. відобразити кафедру з мінімальною кількістю груп")
    print("8. вивести назви предметів, які викладає конкретний викладач")
    print("9. вивести назви кафедр, на яких викладається конкретна дисципліна")
    print("10. вивести назви груп, що належать до конкретного факультету")
    print("11. вивести назви предметів та повні імена викладачів, які читають найбільшу кількість лекцій з них")
    print("12. вивести назву предмету, за яким читається найменше лекцій")
    print("13. вивести назву предмету, за яким читається найбільше лекцій")

    print("0. Вийти")
    choice = input("Оберіть опцію: ")

    if choice == "1":
        report_groups_info()
    elif choice == "2":
        report_teachers_info()
    elif choice == "3":
        report_departments_names()
    elif choice == "4":
        report_group_teachers()
    elif choice == "5":
        report_department_groups()
    elif choice == "6":
        report_max_groups_department()
    elif choice == "7":
        report_min_groups_department()
    elif choice == "8":
        report_teacher_subjects()
    elif choice == "9":
        report_subject_departments()
    elif choice == "10":
        report_faculty_groups()
    elif choice == "11":
        report_teachers_max_subject_lectures()
    elif choice == "12":
        report_subjects_with_min_lectures_count()
    elif choice == "13":
        report_subjects_with_max_lectures_count()

    elif choice == "0":
        break
    else:
        print("Невірний вибір. Будь ласка, оберіть знову.")

# Закриваємо сесію
session.close()
