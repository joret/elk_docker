import redis
import time
#from random import uniform
import random

redis_con = redis.StrictRedis(host='localhost', port=6379, db=0)

while True:
    redis_con.set('foo', 'bar')
    ad_id = int(random.uniform(1, 100))
    user_id = int(random.uniform(1, 5))
    key = '{}:{}'.format(user_id, ad_id)
    redis_con.set(key, 'text' + str(ad_id))
    print('Ad:{} inserted'.format(key))
    time.sleep(1)
#redis_con.get('foo')

