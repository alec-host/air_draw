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
from entries_schema import CreateAndUpdateDrawEntries
from entries_model import DrawManifestDescription

date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#-.method: get entries based on package.
def _get_entries(session: Session,_package,_amount):
	try:
		draw_entries = session.query(DrawManifestDescription.entries,DrawManifestDescription.tier,DrawManifestDescription.period_in_months).where(func.lower(DrawManifestDescription.package)==_package.lower(),DrawManifestDescription.cost==_amount).first()
		if(draw_entries is None):
			return None
		else:
			return draw_entries['entries'],draw_entries['tier'],draw_entries['period_in_months']
	except Exception as ex:
		logger.debug(ex)
		raise ex
	finally:
		session.close()
		
	