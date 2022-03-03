'''
@author: alec_host
'''
import sys
import aiohttp
import requests

from fastapi import APIRouter,Depends,HTTPException
from fastapi_utils.cbv import cbv
from sqlalchemy.orm import Session
from draw_crud import _draw_winner,_get_winner_info,_record_winner
from draw_schema import CreateAndUpdateDrawFinalPoolEntries

from conn.database import DatabaseManager
from conn.redis_wrapper import RedisCache

import conn.config

redis_cache = RedisCache()
draw_router = APIRouter()

db_mgt_1 = DatabaseManager(conn.config.MYSQL_DBASE)

@cbv(draw_router)
class FinalDraw:
	"""
	@draw_router.on_event('startup')
	async def startup_event():
		await redis_cache.init_redis_cache()

	@draw_router.on_event('shutdown')
	async def startup_event():
		await redis_cache.close()
	"""
	session_1: Session = Depends(db_mgt_1.get_db)

	#-.create customer wallet.
	@draw_router.get("/getFinalDrawWinner/{_tier}")
	async def _get_draw_winner(self,_tier: int):
		try:
			#-.method call.
			ticket_no = _draw_winner(self.session_1,_tier)
			
			if (ticket_no is not None):
				_record_winner(self.session_1,ticket_no)
				return {"ERROR":"0","RESULT":"SUCCESS","MESSAGE":str(ticket_no)}
			else:
				return {"ERROR":"1","RESULT":"FAIL","MESSAGE":"Nothing found."}
		except Exception as ex:
			raise HTTPException(**ex.__dict__)

	@draw_router.get("/getWinnerDetails/{_ticket_no}")
	async def _get_winner_details(self,_ticket_no: str):
		try:
			#-.method call.
			response = _get_winner_info(self.session_1,_ticket_no)
			
			if (response is not None):
				return {"ERROR":"0","RESULT":"SUCCESS","MESSAGE":str(response)}
			else:
				return {"ERROR":"1","RESULT":"FAIL","MESSAGE":"Nothing found."}
		except Exception as ex:
			raise HTTPException(**ex.__dict__)