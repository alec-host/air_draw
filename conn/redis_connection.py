'''
@author: alec_host
'''

import redis
import config

connection = None
def connect_to_redis():
    global connection
    connection = redis.StrictRedis(host=config.REDIS_HOST, port=config.REDIS_PORT, password=config.REDIS_PASS, decode_responses=True)

    return connection