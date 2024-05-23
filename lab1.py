from sqlalchemy import create_engine, MetaData, insert, delete, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm import declarative_base
import json

with open("config.json", "r") as f:
    data = json.load(f)
    db_user = data['user']
    db_password = data['password']

db_url = f'postgresql+psycopg2://{db_user}:{db_password}@localhost:5432/hospital'
engine = create_engine(db_url)

# Base = declarative_base()
metadata = MetaData()
metadata.reflect(bind=engine)

connection = engine.connect()


def insert_row(table):
    values = {}

    for column_name in table.columns.keys():
        value = input(f'Enter the value for the {column_name}: ')

        if value != "":
            values[column_name] = value

    query = insert(table).values(values)
    print(query)
    connection.execute(query)
    connection.commit()
    print("Done")


def update_data(table):
    print("Columns names:")
    for column_name in table.columns.keys():
        print('\t', column_name)
    condition_column = input("Enter the column name for condition: ")
    condition_value = input("Enter the condition value for the column: ")

    values = {}

    for column_name in table.columns.keys():
        value = input(f'Enter the value for the {column_name}: ')

        if value != "":
            values[column_name] = value

    column = getattr(table.c, condition_column)
    query = update(table).where(column == column.type.python_type(condition_value)).values(values)
    print(query)
    connection.execute(query)
    connection.commit()
    print("Done")


def delete_record(table):
    print("Columns names:")
    for column_name in table.columns.keys():
        print('\t', column_name)
    # condition_column = input("Enter the column name for condition: ")
    # condition_value = input("Enter the condition value for the column: ")
    # column = getattr(table.c, condition_column)
    # query = delete(table).where(column == column.type.python_type(condition_value))

    condition = input("Enter condition for one column: ")
    #table.c.premium > 100
    query = delete(table).where(eval('table.c.' + condition))
    print(query)
    connection.execute(query)
    connection.commit()
    print("Done")


while True:

    print("Tables from 'hospital': ")
    for table_name in metadata.tables.keys():
        print(table_name)

    table_name = input("Enter table name: ")
    if table_name in metadata.tables.keys():
        table = metadata.tables[table_name]

        print("Select the operation")
        print("1. Add record")
        print("2. Delete record")
        print("3. Update record")

        command = input("Enter the operation number: ")
        if command == "exit":
            break

        if command == "1":
            insert_row(table)

        elif command == "2":
            delete_record(table)

        elif command == "3":
            update_data(table)

