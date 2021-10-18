import sys
sys.path.append(".")

from sqlalchemy import create_engine
from sqlalchemy import select
from sqlalchemy.orm import Session

from orm_skel import Base, Student, add_students, print_students

echo = False

# engine = create_engine('sqlite://', echo=echo)
engine = create_engine('postgresql://admin:password@localhost:5432/sqlalchemy', echo=echo)

Base.metadata.create_all(engine)

add_students(engine)
breakpoint()

# stmt = select(student_table).where(student_table.c.name == 'alice')
stmt = select(Student).where(Student.name == 'alice')
print(stmt)
with Session(engine) as session:
    for row in session.execute(stmt):
        (student, ) = row
        print(row, type(student))

print("\n\nSelecting individual columns:")
print(select(Student.name))

Base.metadata.drop_all(engine)
