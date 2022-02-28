'''
@author: alec_host
'''

import sys
import aiohttp
import requests

from fastapi import APIRouter,Depends,HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from register_crud import _customer_payment_details
from register_schema import CreateAndUpdateCustomerEntries

import conn.config
sys.path.insert(0,conn.config.ENTRIES_DIR)
from entries_crud import _get_entries

from database import DatabaseManager
from redis_wrapper import RedisCache

redis_cache = RedisCache()
register_router = APIRouter()

db_mgt_1 = DatabaseManager(conn.config.MYSQL_DBASE)

@cbv(register_router)
class CustomerEntriesAccount:

	"""
	@register_router.on_event('startup')
	async def startup_event():
		await redis_cache.init_redis_cache()

	@register_router.on_event('shutdown')
	async def startup_event():
		await redis_cache.close()
	"""

	session_1: Session = Depends(db_mgt_1.get_db)

	#-.create customer wallet.
	@register_router.post("/createCustomerEntry/")
	async def _record_customer_entries(self,customer_info: CreateAndUpdateCustomerEntries):
		try:
			#-.method call.
			draw_entries = _get_entries(self.session_1,customer_info.tier,customer_info.package,customer_info.amount)
			#-.loop upto no of entries.
			#-.method call.
			response = _customer_payment_details(self.session_1,customer_info,draw_entries)
			
			if (response is not None):
				return {"ERROR":"0","RESULT":"SUCCESS","MESSAGE":"Customer draw entries recorded successful."}
			else:
				return {"ERROR":"1","RESULT":"FAIL","MESSAGE":"Customer has existing draw entries."}
		except Exception as ex:
			raise HTTPException(**ex.__dict__)