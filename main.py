from sqlalchemy import create_engine, Column, Integer, String, Sequence, Date
from sqlalchemy.orm import sessionmaker
from sqlalchemy import or_, and_, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json

with open("config.json", "r") as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/People'
engine = create_engine(db_url)

Base = declarative_base()


# create table users

class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, Sequence('person_id_sec'), primary_key=True)
    first_name = Column(String(20))
    last_name = Column(String(20))
    city = Column(String(50))
    country = Column(String(50))
    birthday = Column(Date)


# add table to db
#Base.metadata.create_all(bind=engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# add records
person1 = Person(first_name='John', last_name='Doe', city='Kyiv', country="Ukraine", birthday='01-01-2000')
person2 = Person(first_name='Mary', last_name='Doe', city='Kyiv', country="Ukraine", birthday='01-01-2000')

# session.add_all([person1, person2])
# session.add(person1)
# session.add(person2)
# session.commit()


while True:
    print("Chose the command: ")
    print("1. Execute request")
    print("2. All people")
    print("3. All people from the entered city")
    print("4. All people from the entered city or country")
    print("5. All people with first_name starts from the entered letter")
    print("6. Add new record")
    print("7. Update record")
    print("8. Delete record")

    command = input("Command number: ")
    if command == 'exit':
        break

    if command == '1':
        user_query = input("Write request: ")
        result = session.execute((text(user_query)))
        for person in result:
            print(person)

    elif command == '2':
        result = session.query(Person).all()

        for person in result:
            print(person)

    elif command == '3':
        city = input("Enter the city: ")
        #result = session.query(Person).filter_by(city=city).all()
        result = session.query(Person).filter(Person.city == city).all()
        for person in result:
            print(person.first_name, person.last_name)

    elif command == '4':
        city = input("Enter the city: ")
        country = input("Enter the country: ")
        result = session.query(Person).filter(or_(Person.city == city, Person.country == country)).all()

        for person in result:
            print(person.first_name, person.last_name)

    elif command == '5':
        letter = input("Enter the letter: ")
        result = session.query(Person).filter(Person.first_name.like(f'{letter}%')).all()

        for person in result:
            print(person.first_name, person.last_name)

    elif command == '6':
        person = Person(
            first_name=input("Enter the first name: "),
            last_name=input("Enter the last name: "),
            city=input("Enter the city: "),
            country=input("Enter the country: "),
            birthday=input("Enter the birthday: ")
        )
        session.add(person)
        session.commit()

    elif command == '7':
        first_name = input("Enter the first name: ")
        person = session.query(Person).filter(Person.first_name == first_name).first()

        person.city = input("Enter new city: ")
        session.commit()

    elif command == '8':
        first_name = input("Enter the first name: ")
        person = session.query(Person).filter(Person.first_name == first_name).first()

        session.delete(person)
        session.commit()

    else:
        print("Unknown command")

session.close()