from sqlalchemy import create_engine, text

engine = create_engine('sqlite://', echo=True)

with engine.connect() as conn:
    print(engine.pool.status())

engine = create_engine('postgresql://admin:password@localhost:5432/sqlalchemy', echo=True)
with engine.connect() as conn:
    print(engine.pool.status())
    conn2 = engine.connect()
    print(engine.pool.status())
    conn2.close()
    print(engine.pool.status())
    conn3 = engine.connect()
    conn4 = engine.connect()
    conn5 = engine.connect()
    conn6 = engine.connect()
    conn7 = engine.connect()
    print(engine.pool.status())
    conn7.close()
    print(engine.pool.status())
    conn6.close()
    conn5.close()
    conn4.close()
    conn3.close()
    conn2.close()
    print(engine.pool.status())

print(engine.pool.status())


# Manually create the pool/driver
if False:
    import sqlalchemy.pool as pool
    import psycopg2

    def getconn():
        c = psycopg2.connect(user='ed', host='127.0.0.1', dbname='test')
        return c

    mypool = pool.QueuePool(getconn, max_overflow=10, pool_size=5)

