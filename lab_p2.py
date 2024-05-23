from sqlalchemy import create_engine, MetaData, insert, delete, update, extract, distinct
from sqlalchemy import or_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import json
from datetime import datetime

with open("config.json", "r") as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/hospital'
engine = create_engine(db_url)

# Base = declarative_base()
metadata = MetaData()
metadata.reflect(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()

docs = metadata.tables['doctors']
specs = metadata.tables['specializations']
docs_specs = metadata.tables['doctors_specializations']
vacation = metadata.tables['vacations']
wards = metadata.tables['wards']
deps = metadata.tables['departments']
donations = metadata.tables['donations']
sponsors = metadata.tables['sponsors']


def report_doctor_specializations():
    result = session.query(docs.c.name, docs.c.surname, specs.c.name) \
        .join(docs_specs, docs_specs.c.doctor_id == docs.c.id) \
        .join(specs, docs_specs.c.specialization_id == specs.c.id).all()

    if result:
        for row in result:
            print(f"{row.surname} {row.name}")


def report_doctors_salary_not_on_vacation():
    result = session.query(docs.c.surname, docs.c.salary, docs.c.premium) \
        .outerjoin(vacation, vacation.c.doctor_id == docs.c.id).filter(
        or_(datetime.now() < vacation.c.start_date, datetime.now() > vacation.c.end_date))
    print(result)
    if result:
        for row in result:
            print(f"{row.surname} {row.salary} {row.premium}")


def report_wards_department():
    dep = input("Enter department name: ")
    result = session.query(wards.c.name) \
        .join(deps, deps.c.id == wards.c.department_id).where(deps.c.name == dep)

    if result:
        for row in result:
            print(f"{row.name}")


def repor_donation_of_last_mounth():
    user_month = int(input("Enter the month from 1 to 12: "))
    result = session.query(deps.c.name.label("deps_name"), sponsors.c.name, donations.c.amount,
                           donations.c.donation_date) \
        .join(deps, deps.c.id == donations.c.department_id) \
        .join(sponsors, sponsors.c.id == donations.c.sponsor_id) \
        .where(extract("MONTH", donations.c.donation_date) == user_month)

    if result:
        for row in result:
            print(f"{row.deps_name} {row.name} {row.amount} {row.donation_date}")


def report_departaments_donation():
    sponsor_name = input("Enter sponsor name: ")
    result = session.query(deps.c.name) \
        .join(donations, deps.c.id == donations.c.department_id) \
        .join(sponsors, sponsors.c.id == donations.c.sponsor_id) \
        .where(sponsors.c.name == sponsor_name).distinct()
    print(result)
    if result:
        for row in result:
            print(f"{row.name}")


while True:
    print("1. Вивести повні імена лікарів та їх спеціалізації")
    print("2. Вивести прізвища та зарплати лікарів, які не перебувають у відпустці")
    print("3. Вивести назви палат, які знаходяться у певному відділенні;")
    print(
        "4. Вивести усі пожертвування за вказаний місяць у вигляді: відділення, спонсор, сума пожертвування, дата пожертвування;")
    print("5. Вивести назви відділень без повторень, які спонсоруються певною компанією.")

    print("0. Вийти")
    choice = input("Оберіть опцію: ")

    if choice == "1":
        report_doctor_specializations()
    elif choice == "2":
        report_doctors_salary_not_on_vacation()
    elif choice == "3":
        report_wards_department()
    elif choice == "4":
        repor_donation_of_last_mounth()
    elif choice == "5":
        report_departaments_donation()

    elif choice == "0":
        break
    else:
        print("Невірний вибір. Будь ласка, оберіть знову.")

# Закриваємо сесію
session.close()
