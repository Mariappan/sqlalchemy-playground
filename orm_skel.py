from sqlalchemy import create_engine, text
from sqlalchemy import Table, Column, Integer, String
from sqlalchemy.orm import declarative_base

Base = declarative_base()


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True)

    name = Column(String)

    age = Column(Integer)

    def __repr__(self):
        return f"Student(id={self.id!r}, name={self.name!r}, age={self.age!r})"


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
    Base.metadata.create_all(engine)
    add_students(engine)
    print_students(engine)

