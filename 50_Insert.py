import sys
sys.path.append(".")

from sqlalchemy import create_engine, text
from sqlalchemy import insert

from skel import metadata, student_table, print_students

# Print the SQL statement generated
stmt = insert(student_table).values(name='spongebob', age=5)
print(f"Statement is \n{stmt}")

compiled = stmt.compile()
print(f"Compiled Statement is \n{compiled}")
print(compiled.params)

engine = create_engine('sqlite://', echo=True)
# engine = create_engine('postgresql://admin:password@localhost:5432/sqlalchemy', echo=True)
metadata.create_all(engine)

with engine.begin() as conn:
    result = conn.execute(stmt)
    print(f"Inserted: Primary key is {result.inserted_primary_key}")
print_students(engine)

with engine.begin() as conn:
    result = conn.execute(
            insert(student_table),
            [
                {"name": "alice", "age": 14},
                {"name": "bob", "age": 12}
                ]
            )
print_students(engine)

# Cleanup: Drop the table
metadata.drop_all(engine)
