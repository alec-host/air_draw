'''
@author: alec_host
'''
import sys
import aiohttp
import asyncio
import requests

import conn.config

class AT:
	async def _send_message(self,_name,_entries,_msisdn=None):
		if _msisdn is None:
			# don't send my own messages
			return

		if(_name is not None or _name.strip() != ""):
			_first_name = _name.split(" ")[0].strip().capitalize()[0:15]
		else:
			_first_name = "User"
		
		if(int(_entries) > 0):
			inner_text = "entries"
		else:
			inner_text = "entry"
			
		message = conn.config.TEMPLATE_MESSAGE.replace('{0}',str(_first_name)).replace('{1}',str(_entries)).replace('{2}',inner_text)
	
		headers = {
			'apiKey' : conn.config.AT_SMS_KEY,
			'Accept' : 'application/json',
			'username' : conn.config.AT_SMS_USERNAME
		}	
		
		payload = {
			'username' : conn.config.AT_SMS_USERNAME,
			'from' : conn.config.AT_SMS_FROM,
			'keyword' :  conn.config.AT_SMS_KEY,
			'bulkSMSMode' : 1,
			'to' : str(_msisdn),
			'message' : str(message),
		}
			
		response = requests.post(conn.config.AT_ENDPOINT,data=payload,headers=headers)	
		
		return response