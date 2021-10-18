from sqlalchemy import create_engine, MetaData, text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import declarative_base

metadata = MetaData()

student_table = Table(
        "students",
        metadata,
        Column('id', Integer, primary_key=True),
        Column('name', String),
        Column('age', Integer)
        )


def print_students(engine):
    result = engine.execute(text("SELECT * from students"))
    print(result.all())


def add_students(engine):
    with engine.begin() as conn:
        conn.execute(
            text("INSERT INTO students (name, age) VALUES (:name, :age)"),
            [{"name": "alice", "age": 19}, {"name": "bob", "age": 20}]
        )


if __name__ == "__main__":
    engine = create_engine('sqlite://', echo=True)
    metadata.create_all(engine)
    add_students(engine)
    print_students(engine)

