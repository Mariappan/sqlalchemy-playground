from sqlalchemy import create_engine, MetaData, text
from sqlalchemy import Table, Column, Integer, String

def core_metadata(*, engine):
    metadata_obj = MetaData()


    coor_table = Table(
            "coordinates",
            metadata_obj,
            Column('x', Integer, primary_key=True),
            Column('y', Integer)
            )

    print(coor_table.c[0])
    coor_table.c[1]

    # Primary key is stored
    print(coor_table.primary_key)

    # Create all tables using the metadata
    metadata_obj.create_all(engine)

    # Drop all tables
    metadata_obj.drop_all(engine)


sql_engine = create_engine('sqlite://', echo=True)
core_metadata(engine=sql_engine)

postgres_engine = create_engine('postgresql://admin:password@localhost:5432/sqlalchemy', echo=True)
core_metadata(engine=postgres_engine)
breakpoint()

from sqlalchemy.orm import declarative_base
Base = declarative_base()

class Coordinates(Base):
    __tablename__ = 'coordinates'
    x = Column(Integer, primary_key=True)
    y = Column(Integer)
    def __repr__(self):
        return f"Coor(x={self.x}, y={self.y})"

Base.metadata.create_all(postgres_engine)
print(Coordinates.__table__)
print ("Run 41_reflect.py now")
breakpoint()

Base.metadata.drop_all(postgres_engine)
