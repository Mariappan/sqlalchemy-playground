from datetime import date

from sqlalchemy import create_engine, Boolean, select
from sqlalchemy import Column, String, Integer, Date, Table, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship, backref, declarative_base
import typing
import sqlalchemy as sa

postgres_engine = create_engine('postgresql://admin:password@localhost:5432/sqlalchemy', echo=True)
PostgresSession = sessionmaker(bind=postgres_engine)

sqlite_engine = create_engine('sqlite://', echo=True)
SQLiteSession = sessionmaker(bind=sqlite_engine)

Base = declarative_base()

movies_actors_association = Table(
    'movies_actors', Base.metadata,
    Column('movie_id', Integer, ForeignKey('movies.id')),
    Column('actor_id', Integer, ForeignKey('actors.id'))
)


class ModelMixin:
    def __repr__(self) -> str:
        return self._repr(id=self.id)

    def _repr(self, **fields: typing.Dict[str, typing.Any]) -> str:
        field_strings = []
        at_least_one_attached_attribute = False
        for key, field in fields.items():
            try:
                field_strings.append(f'{key}={field!r}')
            except sa.orm.exc.DetachedInstanceError:
                field_strings.append(f'{key}=DetachedInstanceError')
            else:
                at_least_one_attached_attribute = True
        if at_least_one_attached_attribute:
            return f"<{self.__class__.__name__}({','.join(field_strings)})>"
        return f"<{self.__class__.__name__} {id(self)}>"


class Movie(Base, ModelMixin):
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=True)
    title = Column(String)
    release_date = Column(Date)
    actors = relationship("Actor", secondary=movies_actors_association)

    def __init__(self, title, release_date):
        self.title = title
        self.release_date = release_date

    def __repr__(self):
        return self._repr(
            title=self.title,
        )


class Actor(Base, ModelMixin):
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    birthday = Column(Date)

    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday

    def __repr__(self):
        return self._repr(
            name=self.name,
        )


class Stuntman(Base, ModelMixin):
    __tablename__ = 'stuntmen'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Boolean)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref=backref("stuntman", uselist=False))

    def __init__(self, name, active, actor):
        self.name = name
        self.active = active
        self.actor = actor

    def __repr__(self):
        return self._repr(
            name=self.name,
        )


class ContactDetails(Base):
    __tablename__ = 'contact_details'

    id = Column(Integer, primary_key=True)
    phone_number = Column(String)
    address = Column(String)
    actor_id = Column(Integer, ForeignKey('actors.id'))
    actor = relationship("Actor", backref="contact_details")

    def __init__(self, phone_number, address, actor):
        self.phone_number = phone_number
        self.address = address
        self.actor = actor

    def __repr__(self):
        return self._repr(
            name=self.actor.name,
        )

# Cleanup
Base.metadata.drop_all(postgres_engine)

Base.metadata.create_all(postgres_engine)

Base.metadata.create_all(sqlite_engine)

# 4 - create movies
bourne_identity = Movie("The Bourne Identity", date(2002, 10, 11))
furious_7 = Movie("Furious 7", date(2015, 4, 2))
pain_and_gain = Movie("Pain & Gain", date(2013, 8, 23))

# 5 - creates actors
matt_damon = Actor("Matt Damon", date(1970, 10, 8))
dwayne_johnson = Actor("Dwayne Johnson", date(1972, 5, 2))
mark_wahlberg = Actor("Mark Wahlberg", date(1971, 6, 5))

# 6 - add actors to movies
bourne_identity.actors = [matt_damon]
furious_7.actors = [dwayne_johnson]
pain_and_gain.actors = [dwayne_johnson, mark_wahlberg]

# session = SQLiteSession()
session = PostgresSession()

# 9 - persists data
session.add(bourne_identity)
session.add(furious_7)
session.add(pain_and_gain)

# stmt = select(Actor).where(Actor.name == 'Matt Damon')
# a = session.execute(stmt)
# a.all()

breakpoint()
