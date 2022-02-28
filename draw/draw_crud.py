'''
@author: alec_host
'''

import sys
import uuid

from datetime import datetime

from sqlalchemy import or_,desc,func
from sqlalchemy.orm import Session

import conn.config
sys.path.insert(0,conn.config.ENTRIES_DIR)
from draw_schema import CreateAndUpdateDrawFinalPoolEntries, CreateAndUpdateDrawWinners
from draw_model import DrawFinalPoolEntriesDescription, DrawWinnerDescription

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#-.method: get entries based on package.
def _draw_winner(session: Session,_tier: int):
	draw_entries = session.query(DrawFinalPoolEntriesDescription.ticket_no).filter_by(tier=_tier).order_by(func.rand()).first()
	
	if(draw_entries is not None):
		return draw_entries['ticket_no']
	else:
		return None
		
#-.method: get entries based on package.
def _get_winner_info(session: Session,_ticket_no: str):
	customer_info = session.query(DrawWinnerDescription.name,DrawWinnerDescription.msisdn).filter_by(ticket_no=_ticket_no).first()
	
	if(customer_info is not None):
		return customer_info['name'] +'|'+ customer_info['msisdn']
	else:
		return None

#-.method: record winner.
def _record_winner(session: Session,_ticket_no: str) -> DrawWinnerDescription:
	winner_details = session.query(DrawWinnerDescription.msisdn).filter(DrawWinnerDescription.ticket_no==_ticket_no)
	if(int(winner_details.count()) == 0):
		try:
			session.execute('INSERT INTO tbl_draw_winners (`msisdn`,`name`,`ticket_no`,`tier`) (SELECT `msisdn`,`name`,`ticket_no`,`tier` FROM tbl_customer_entries WHERE `ticket_no` = "%s")' % (_ticket_no))
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()
	else:
		customer_info=None
		