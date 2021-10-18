from sqlalchemy import create_engine
from sqlalchemy import func

engine = create_engine('postgresql://admin:password@localhost:5432/sqlalchemy', echo=True)


engine.execute(func.count())
engine.execute(func.maari())
