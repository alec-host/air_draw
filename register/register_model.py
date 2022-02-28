'''
@author: alec_host
'''

import sys
  
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Float, DateTime

import conn.config
sys.path.insert(0,conn.config.CONNECT_DIR)
#sys.path.insert(0,'C:/Python37/workspace/AirdukaLottery/conn/')
from database import Base

class CustomerEntriesDescription(Base):
	__tablename__ = "tbl_customer_entries"
	
	_id = Column(Integer, primary_key=True, index=True)
	
	company_name= Column(String)
	company_identifier = Column(String)
	name = Column(String)
	msisdn = Column(String)
	email = Column(String)
	ticket_no = Column(String)
	amount = Column(Float)
	package = Column(String)
	tier = Column(String)
	date_created = Column(DateTime)
	date_modified = Column(DateTime)
	is_archived = Column(Integer)