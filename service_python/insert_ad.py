import redis
import time
import datetime
import random

redis_con = redis.StrictRedis(host='localhost', port=6379, db=0)
log = open('ad_service.log', 'w')

while True:
    redis_con.set('foo', 'bar')
    ad_id = int(random.uniform(1, 100))
    user_id = int(random.uniform(1, 5))
    key = '{}:{}'.format(user_id, ad_id)
    date = '{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
    log_json = {'service':'ad', 'date':date, 'ad_id': key}
    redis_con.set(key, 'text' + str(ad_id))
    print('Ad:{} inserted'.format(key))
    log.write(str(log_json) + '\n')
    log.flush()
    time.sleep(1)
#redis_con.get('foo')

