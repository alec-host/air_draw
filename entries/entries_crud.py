'''
@author: alec_host
'''

import sys
import uuid

from datetime import datetime

from sqlalchemy import or_,desc
from sqlalchemy.orm import Session

import conn.config
sys.path.insert(0,conn.config.ENTRIES_DIR)
from entries_schema import CreateAndUpdateDrawEntries
from entries_model import DrawEntriesDescription

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#-.method: get entries based on package.
def _get_entries(session: Session,months,package,amount):
	draw_entries = session.query(DrawEntriesDescription.entries).filter_by(period_in_months=months,package=package,cost=amount).first()
	
	return draw_entries['entries']