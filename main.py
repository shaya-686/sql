from sqlalchemy import create_engine, Column, Integer, String, Numeric, Sequence, Date, Enum, ForeignKey
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import or_, and_, func
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import text
import json
from datetime import datetime

with open("config.json", "r") as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/Sales'
engine = create_engine(db_url)

Base = declarative_base()


class Sales(Base):
    __tablename__ = 'sales'
    id = Column(Integer, Sequence('sale_id_sec'), primary_key=True)
    amount = Column(Integer)
    create_date = Column(Date)
    customer_id = Column(Integer, ForeignKey('customers.id'))
    salesman_id = Column(Integer, ForeignKey('salesmen.id'))

    salesman = relationship("Salesmen", back_populates="sale")
    customer = relationship("Customers", back_populates="sale")

    def __str__(self):
        return f'id: {self.id}, amount: {self.amount}, create_date: {self.create_date}'


class Salesmen(Base):
    __tablename__ = 'salesmen'
    id = Column(Integer, Sequence('salesmen_id_sec'), primary_key=True)
    first_name = Column(String(20))
    second_name = Column(String(20))
    contact_phone = Column(String(20), unique=True)

    sale = relationship("Sales", back_populates="salesman")

    def __str__(self):
        return f'First name: {self.first_name}, last name: {self.second_name}, phone: {self.contact_phone}'


class Customers(Base):
    __tablename__ = 'customers'
    id = Column(Integer, Sequence('customer_id_sec'), primary_key=True)
    first_name = Column(String(20))
    second_name = Column(String(20))
    contact_phone = Column(String(20), unique=True)

    sale = relationship("Sales", back_populates="customer")

    def __str__(self):
        return f'First name: {self.first_name}, last name: {self.second_name}, phone: {self.contact_phone}'


# add table to db
#Base.metadata.create_all(bind=engine)

# create session
Session = sessionmaker(bind=engine)
session = Session()

# add records
first_salesman = Salesmen(first_name="John", second_name="Doe", contact_phone="380222222222")
second_salesman = Salesmen(first_name="Mary", second_name="Smith", contact_phone="380777777777")

first_customer = Customers(first_name="Bob", second_name="Smith", contact_phone="380111111111")
second_customer = Customers(first_name="Elly", second_name="Black", contact_phone="380133111111")
third_customer = Customers(first_name="Kyle", second_name="Smith", contact_phone="380111441111")

first_order = Sales(amount=234, create_date='01-01-2024', customer_id=6, salesman_id=4)
third_order = Sales(amount=800, create_date='01-02-2024', customer_id=5, salesman_id=5)
second_order = Sales(amount=300, create_date='01-03-2024', customer_id=5, salesman_id=4)
#session.add_all([first_salesman, second_salesman, first_customer, second_customer, third_customer])
#session.add_all([first_order, second_order, third_order])
#session.commit()


while True:
    print("Chose the command: ")
    print("1. Select all orders")
    print("2. Select all salesman orders")
    print("3. Select order with the max amount")
    print("4. Select order with the min amount")
    print("5. Select order with the max amount for salesman")
    print("6. Select order with the min amount for salesman")
    print("7. Select order with the max amount for customer")
    print("8. Select order with the min amount for customer")
    print("9. Select salesman with the max order amount")
    print("10. Select salesman with the min order amount")
    print("11. Select customer with the max order amount")
    print("12. Select customer with the min order amount")
    print("13. Select avg order amount for customer")
    print("14. Select avg order amount for salesman")
    print("15. Add new customer")
    print("16. Add new salesman")
    print("17. Add new sale")
    print("18. Update customer")
    print("19. Update salesman")
    print("20. Update sale")
    print("21. Delete customer")
    print("22. Delete salesman")
    print("23. Delete sale")

    command = input("Command number: ")
    if command == 'exit':
        break

    if command == '1':
        result = session.query(Sales).all()

        for order in result:
            print(order)

    elif command == '2':
        phone = input("Enter the salesman contact phone: ")
        result = session.query(Sales).join(Salesmen).filter(Salesmen.contact_phone == phone).all()

        for order in result:
            print(order)

    elif command == '3':
        max_amount = session.query(func.max(Sales.amount)).scalar()
        order = session.query(Sales).filter(Sales.amount == max_amount).first()
        print(order)

    elif command == '4':
        min_amount = session.query(func.min(Sales.amount)).scalar()
        order = session.query(Sales).filter(Sales.amount == min_amount).first()
        print(order)

    elif command == '5':
        phone = input("Enter the salesman contact phone: ")
        max_amount = session.query(func.max(Sales.amount)).join(Salesmen).filter(
            Salesmen.contact_phone == phone).scalar()
        result = session.query(Sales).join(Salesmen).filter(Salesmen.contact_phone == phone,
                                                            Sales.amount == max_amount).all()

        for order in result:
            print(order)

    elif command == '6':
        phone = input("Enter the salesman contact phone: ")
        min_amount = session.query(func.min(Sales.amount)).join(Salesmen).filter(
            Salesmen.contact_phone == phone).scalar()
        result = session.query(Sales).join(Salesmen).filter(Salesmen.contact_phone == phone,
                                                            Sales.amount == min_amount).all()

        for order in result:
            print(order)

    elif command == '7':
        phone = input("Enter the customer contact phone: ")
        max_amount = session.query(func.max(Sales.amount)).join(Customers).filter(
            Customers.contact_phone == phone).scalar()
        result = session.query(Sales).join(Customers).filter(Customers.contact_phone == phone,
                                                             Sales.amount == max_amount).all()

        for order in result:
            print(order)

    elif command == '8':
        phone = input("Enter the customer contact phone: ")
        min_amount = session.query(func.min(Sales.amount)).join(Customers).filter(
            Customers.contact_phone == phone).scalar()
        result = session.query(Sales).join(Customers).filter(Customers.contact_phone == phone,
                                                             Sales.amount == min_amount).all()

        for order in result:
            print(order)

    elif command == '9':
        total_for_all = session.query(func.sum(Sales.amount)).join(Salesmen).group_by(Salesmen.contact_phone).all()
        max_amount = max(total[0] for total in total_for_all)
        max_salesmen = session.query(Salesmen.contact_phone).join(Sales).group_by(Salesmen.contact_phone).having(
            func.sum(Sales.amount) == max_amount).all()
        result = session.query(Salesmen).filter(Salesmen.contact_phone.in_(phone[0] for phone in max_salesmen)).all()
        for salesman in result:
            print(salesman)

    elif command == '10':
        total_for_all = session.query(func.sum(Sales.amount)).join(Salesmen).group_by(Salesmen.contact_phone).all()
        min_amount = min(total[0] for total in total_for_all)
        min_salesmen = session.query(Salesmen.contact_phone).join(Sales).group_by(Salesmen.contact_phone).having(
            func.sum(Sales.amount) == min_amount).all()
        result = session.query(Salesmen).filter(Salesmen.contact_phone.in_(phone[0] for phone in min_salesmen)).all()
        for salesman in result:
            print(salesman)

    elif command == '11':
        total_for_all = session.query(func.sum(Sales.amount)).join(Customers).group_by(Customers.contact_phone).all()
        max_amount = max(total[0] for total in total_for_all)
        max_customers = session.query(Customers.contact_phone).join(Sales).group_by(Customers.contact_phone).having(
            func.sum(Sales.amount) == max_amount).all()
        result = session.query(Customers).filter(Customers.contact_phone.in_(phone[0] for phone in max_customers)).all()
        for customer in result:
            print(customer)

    elif command == '12':
        total_for_all = session.query(func.sum(Sales.amount)).join(Customers).group_by(Customers.contact_phone).all()
        min_amount = min(total[0] for total in total_for_all)
        min_customers = session.query(Customers.contact_phone).join(Sales).group_by(Customers.contact_phone).having(
            func.sum(Sales.amount) == min_amount).all()
        result = session.query(Customers).filter(Customers.contact_phone.in_(phone[0] for phone in min_customers)).all()
        for customer in result:
            print(customer)

    elif command == '13':
        phone = input("Enter the customer contact phone: ")
        avg_amount = round(session.query(func.avg(Sales.amount)).join(Customers).filter(
            Customers.contact_phone == phone).scalar(), 2)

        print(avg_amount)

    elif command == '14':
        phone = input("Enter the salesman contact phone: ")
        avg_amount = round(session.query(func.avg(Sales.amount)).join(Salesmen).filter(
            Salesmen.contact_phone == phone).scalar(), 2)

        print(avg_amount)

    elif command == '15':
        customer = Customers(
            first_name=input("Enter the first name: "),
            second_name=input("Enter the last name: "),
            contact_phone=input("Enter the phone: "),
        )
        session.add(customer)
        session.commit()

    elif command == '16':
        salesman = Salesmen(
            first_name=input("Enter the first name: "),
            second_name=input("Enter the last name: "),
            contact_phone=input("Enter the phone: "),
        )
        session.add(salesman)
        session.commit()

    elif command == '17':
        amount = int(input("Enter the amount: "))
        customer_phone = input("Enter the customer phone: ")
        customer_id = session.query(Customers.id).filter(Customers.contact_phone == customer_phone).first()
        if not customer_id:
            print("Customer not found")
            continue
        salesman_phone = input("Enter the salesman phone: ")
        salesman_id = session.query(Salesmen.id).filter(Salesmen.contact_phone == salesman_phone).first()
        if not salesman_id:
            print("Salesman not found")
            continue

        sale = Sales(amount=amount, create_date=datetime.now(), customer_id=customer_id[0], salesman_id=salesman_id[0])
        session.add(sale)
        session.commit()

    elif command == '18':
        phone = input("Enter customer phone: ")
        customer = session.query(Customers).filter(Customers.contact_phone == phone).first()

        customer.second_name = input("Enter new second name: ")
        session.commit()

    elif command == '19':
        phone = input("Enter salesman phone: ")
        salesman = session.query(Salesmen).filter(Salesmen.contact_phone == phone).first()

        salesman.second_name = input("Enter new second name: ")
        session.commit()

    elif command == '20':
        order_id = input("Enter the order id: ")
        sale = session.query(Sales).filter(Sales.id == order_id).first()

        sale.amount = int(input("Enter the new amount: "))
        session.commit()

    elif command == '21':
        phone = input("Enter customer phone: ")
        customer = session.query(Customers).filter(Customers.contact_phone == phone).first()
        if not customer:
            print("Customer not found")
            continue
        sales = session.query(Sales.id).filter(Sales.customer_id == customer.id).first()
        if sales:
            print("Customer couldn't be deleted")
            continue

        session.delete(customer)
        session.commit()

    elif command == '22':
        phone = input("Enter salesman phone: ")
        salesman = session.query(Salesmen).filter(Salesmen.contact_phone == phone).first()
        if not salesman:
            print("Salesman not found")
            continue
        sales = session.query(Sales.id).filter(Sales.salesman_id == salesman.id).first()
        if sales:
            print("Salesman couldn't be deleted")
            continue

        session.delete(salesman)
        session.commit()

    elif command == '23':
        order_id = input("Enter the order id: ")
        order = session.query(Sales).filter(Sales.id == order_id).first()
        if not order:
            print("Order not found")
            continue

        session.delete(order)
        session.commit()

    else:
        print("Unknown command")

session.close()
