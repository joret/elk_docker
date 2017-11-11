import redis
import time
import random
import datetime

redis_con = redis.StrictRedis(host='localhost', port=6379, db=0)
log = open('delete_service.log', 'w')
while True:
    ad_id = int(random.uniform(1, 100))
    user_id = int(random.uniform(1, 5))
    key = '{}:{}'.format(user_id, ad_id)
    exists = redis_con.get(key)
    if exists != None:
        date = 'Timestamp:{:%Y-%m-%d %H:%M:%S}'.format(datetime.datetime.now())
        res = redis_con.delete(exists)
        print(str(res))
        log.write('{} Deleated ad_id:{}\n'.format(date, key))
        log.flush()
    else:
        print('Not found:' + str(key))
    time.sleep(1)
#redis_con.get('foo')

