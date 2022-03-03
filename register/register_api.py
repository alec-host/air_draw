'''
@author: alec_host
'''
import sys
import aiohttp
import requests

from fastapi import APIRouter,Depends,HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from register_crud import _customer_payment_details,_customer_entries
from register_schema import CreateAndUpdateCustomerEntries,SearchValidationStub

import conn.config
sys.path.insert(0,conn.config.ENTRIES_DIR)
from entries_crud import _get_entries

from conn.database import DatabaseManager
from conn.redis_wrapper import RedisCache

from sms.at_sms import AT

redis_cache = RedisCache()
register_router = APIRouter()

db_mgt_1 = DatabaseManager(conn.config.MYSQL_DBASE)

@cbv(register_router)
class CustomerEntriesAccount:

	"""
	changes on register_api & 
	@register_router.on_event('startup')
	async def startup_event():
		await redis_cache.init_redis_cache()

	@register_router.on_event('shutdown')
	async def startup_event():
		await redis_cache.close()
	"""

	session_1: Session = Depends(db_mgt_1.get_db)

	#-.create customer wdraw entries.
	@register_router.post("/createCustomerEntry/")
	async def _record_customer_entries(self,customer_info: CreateAndUpdateCustomerEntries):
		try:
			#-.method call.
			draw_configs = _get_entries(self.session_1,customer_info.package,customer_info.amount)
			if(draw_configs is not None):
				#-.method call.
				response = _customer_payment_details(self.session_1,customer_info,draw_configs[0],draw_configs[1])
				if (response is not None):
					at = AT()
					resp = await at._send_message(customer_info.name,draw_configs[0],customer_info.msisdn)				
					return {"ERROR":"0","RESULT":"SUCCESS","MESSAGE":"Customer draw entries recorded successful."}
				else:
					return {"ERROR":"1","RESULT":"FAIL","MESSAGE":"Customer has existing draw entries."}
			else:
				return {"ERROR":"1","RESULT":"FAIL","MESSAGE":"Something wrong happened. Check tbl_draw_manifest"}
		except Exception as ex:
			raise HTTPException(**ex.__dict__)
			
	#-.get customer draw entries.
	@register_router.post("/getCustomerEntries/")
	async def _get_customer_entries(self,search_input: SearchValidationStub):
		try:
			_limit = 1000
			#-.method call.
			print('j=here to the world' + str(search_input.search))
			entries = _customer_entries(self.session_1,search_input.search,_limit)
			if (len(entries) > 0):
				#return {"ERROR":"0","RESULT":"SUCCESS","DATA":entries,"MESSAGE":"Customer draw entries recorded successful."}
				return {"Result":"OK","Records":entries,"TotalRecordCount":len(entries)}
			else:
				#return {"ERROR":"1","RESULT":"FAIL","MESSAGE":"No customer entries."}
				return {"Result":"OK","Records":[],"TotalRecordCount":0}
		except Exception as ex:
			raise HTTPException(**ex.__dict__)