import sys
sys.path.append(".")

from sqlalchemy import create_engine
from sqlalchemy import select

from skel import metadata, student_table, add_students, print_students


echo = False

# engine = create_engine('sqlite://', echo=echo)
engine = create_engine('postgresql://admin:password@localhost:5432/sqlalchemy', echo=echo)

metadata.create_all(engine)

add_students(engine)
breakpoint()

stmt = select(student_table).where(student_table.c.name == 'alice')
print(stmt)

with engine.connect() as conn:
    for row in conn.execute(stmt):
        print(row)
        print(row.name, row.age, row[0])
        print(f"Type is {type(row)}")

print("\n\nSelecting individual columns:")
print(select(student_table.c.name))

metadata.drop_all(engine)
