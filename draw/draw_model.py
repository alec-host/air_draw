'''
@author: alec_host
'''

import sys
  
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Float, DateTime

import conn.config
sys.path.insert(0,conn.config.CONNECT_DIR)

from database import Base

class DrawFinalPoolEntriesDescription(Base):
	__tablename__ = "tbl_draw_entries"
	
	_id = Column(Integer, primary_key=True, index=True)
	
	msisdn = Column(String)
	ticket_no = Column(String)
	tier = Column(Integer)
	
class DrawWinnerDescription(Base):
	__tablename__ = "tbl_draw_winners"
	
	_id = Column(Integer, primary_key=True, index=True)
	
	msisdn = Column(String)
	name = Column(String)
	ticket_no = Column(String)
	tier = Column(Integer)