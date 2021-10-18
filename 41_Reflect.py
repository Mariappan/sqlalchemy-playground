from sqlalchemy import create_engine, MetaData, text
from sqlalchemy import Table, Column, Integer, String

meta = MetaData()
engine = create_engine('postgresql://admin:password@localhost:5432/sqlalchemy', echo=True)


t = Table('coordinates', meta, autoload_with=engine)

breakpoint()
