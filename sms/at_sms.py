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
			
		message = conn.config.TEMPLATE_MESSAGE.replace('{0}',str(_name)).replace('{1}',str(_entries))
	
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
		#connector = aiohttp.TCPConnector(verify_ssl=False)
		#asyncio.ensure_future(
		#aiohttp.request('post', url, data = payload, headers = headers, connector=connector)
		#).add_done_callback(lambda future: future.result()) 