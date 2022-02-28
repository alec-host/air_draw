'''
@author: alec_host
'''

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

import config

Base = declarative_base()

class DatabaseManager:
    url = None
    SessionLocal = None
    def __init__(self, url):
        self.url = url
        db_engine = create_engine(config.MYSQL_URL+self.url)
        self.SessionLocal = sessionmaker(autocommit=False,autoflush=False,bind=db_engine)

    def get_db(self):
        db = None

        try:
            db = self.SessionLocal()
            yield db
        finally:
            db.close()