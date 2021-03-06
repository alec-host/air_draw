'''
@author: alec_host
'''
import sys

import conn.config
  
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Float, DateTime
sys.path.insert(0,conn.config.CONNECT_DIR)
from conn.database import Base

class DrawManifestDescription(Base):
	__tablename__ = "tbl_draw_manifest"
	
	_id = Column(Integer, primary_key=True, index=True)
	
	period_in_months = Column(String)
	package = Column(String)
	cost = Column(Float)
	entries = Column(Integer)
	tier = Column(Integer)
	validity_in_month = Column(Integer)
	is_deleted = Column(Integer)