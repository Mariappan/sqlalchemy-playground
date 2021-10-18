from sqlalchemy import create_engine, text
from sqlalchemy.orm import Session

print (f"\n SQLite DB\n")
engine = create_engine('sqlite://', echo=True)

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE coordinates (x int, y int)"))
    conn.execute(
        text("INSERT INTO coordinates (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )
    result = conn.execute(text("select * from coordinates"))
    print(result.all())


# Postgres Engine
print (f"\n PostgreSQL DB\n")
engine = create_engine('postgresql://admin:password@localhost:5432/sqlalchemy', echo=True)
with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())

with engine.connect().execution_options(autocommit=False) as conn:
    conn.execute(text("CREATE TABLE coordinates (x int, y int)"))
    conn.execute(
        text("INSERT INTO coordinates (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )

with engine.connect() as conn:
    conn.execute(text("CREATE TABLE coordinates (x int, y int)"))
    conn.execute(
        text("INSERT INTO coordinates (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )

# Cleanup
with engine.connect() as conn:
    conn.execute(text("DROP TABLE coordinates"))

# Using begin - transaction with autocommit
with engine.begin() as conn:
    conn.execute(text("CREATE TABLE coordinates (x int, y int)"))
    conn.execute(
        text("INSERT INTO coordinates (x, y) VALUES (:x, :y)"),
        [{"x": 1, "y": 1}, {"x": 2, "y": 4}]
    )

# Using ORM Session
with Session(engine) as session:
    result = session.execute(
            text("UPDATE coordinates SET y=:y WHERE x=:x"),
            [{"x": 9, "y":11}, {"x": 13, "y": 15}]
            )
    result = session.execute(
            text("UPDATE coordinates SET y=:y WHERE x=:x"),
            [{"x": 10, "y":13}, {"x": 15, "y": 17}]
            )

with Session(engine) as session:
    result = session.execute(
            text("UPDATE coordinates SET y=:y WHERE x=:x"),
            [{"x": 9, "y":11}, {"x": 13, "y": 15}]
            )
    result = session.execute(
            text("UPDATE coordinates SET y=:y WHERE x=:x"),
            [{"x": 10, "y":13}, {"x": 15, "y": 17}]
            )
    session.commit()

# Cleanup
with engine.begin() as conn:
    conn.execute(text("DROP TABLE coordinates"))

