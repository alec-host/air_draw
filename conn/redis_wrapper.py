'''
@author: alec_host
'''

import logging
import aioredis

import conn.config

from typing import Optional
from aioredis import Redis,create_redis_pool

log=logging.getLogger(__name__)

#from configs.freknur_settings import redis_params,redis_key_params

class RedisCache():
    
    def __init__(self):
        self.redis_cache: Optional[Redis] = None
    
    #-.init cache.
    async def init_redis_cache(self):
       self.redis_cache = await create_redis_pool((conn.config.REDIS_HOST,conn.config.REDIS_PORT),db=0,password=conn.config.REDIS_PASS)
    
    async def keys(self,pattern):
        return await self.redis_cache.keys(pattern)

    #-.write to redis.
    async def _set(self,key,data):
        return await self.redis_cache.set(key,data)

    #-.read redis.
    async def _get(self,key):
        return await self.redis_cache.get(key)

    #-.delete data from redis.
    async def _del(self,key):
        return await self.redis_cache.delete(key)

    #-.close redis.
    async def close(self):
        self.redis_cache.close()
        await self.redis_cache.wait_closed()

    #-.redis key.
    def _store(self):
        return [conn.config.OOWALLET_BAL_KEY,conn.config.OOPORTFOLIO_KEY,conn.config.OOASSET_STMT_KEY,conn.config.OOLOAN_STMT_KEY,conn.config.OOWALLET_STMT_KEY,conn.config.OOSHOP_LIST_KEY,conn.config.OOASSET_LIST_KEY,conn.config.OOPUSH_MESSAGE_KEY]


redis_cache = RedisCache()