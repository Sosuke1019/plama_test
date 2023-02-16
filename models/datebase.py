from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

datebase_file = os.path.join(os.path.abpath(os.path.dirname(__file__)), 'plama.db')
engine = create_engine('sqlite:///' + datebase_file, convert_unicode=True)
db_session = scoped_session(sessionmaker(autocommit=False, autoflush=False,bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
    import models.models
    Base.metadata.create_all(bind=engine)