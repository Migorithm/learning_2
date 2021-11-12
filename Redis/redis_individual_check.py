import redis

rc1 = redis.Redis.from_url("redis://upgrade-test5-0001-001.kitlrm.0001.apn2.cache.amazonaws.com:6379",socket_connect_timeout=0.5,retry_on_timeout=False)
rc2 = redis.Redis.from_url("redis://upgrade-test5-0001-002.kitlrm.0001.apn2.cache.amazonaws.com:6379",socket_connect_timeout=0.5,retry_on_timeout=False)
rc3 = redis.Redis.from_url("redis://upgrade-test5-0002-001.kitlrm.0001.apn2.cache.amazonaws.com:6379",socket_connect_timeout=0.5,retry_on_timeout=False)
rc4 = redis.Redis.from_url("redis://upgrade-test5-0002-002.kitlrm.0001.apn2.cache.amazonaws.com:6379",socket_connect_timeout=0.5,retry_on_timeout=False)

while all([rc1.ping(),rc2.ping(),rc3.ping(),rc4.ping()]):
    print("connected to redis1 {}".format(rc1))
    print("connected to redis2 {}".format(rc1))
    print("connected to redis3 {}".format(rc1))
    print("connected to redis4 {}".format(rc1))

    continue
else:
    #to check wich node incurred the problem
    print("connection to rc1 : " , str(rc1.ping()))
    print("connection to rc2 : " , str(rc2.ping()))
    print("connection to rc3 : " , str(rc3.ping()))
    print("connection to rc4 : " , str(rc4.ping()))
    raise Exception("At least one of them has been disconnected")
