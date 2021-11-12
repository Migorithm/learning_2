#!/Users/we/google_course/venv/bin/python3
from rediscluster import RedisCluster
import string
rc = RedisCluster.from_url("redis://upgrade-test50.kitlrm.clustercfg.apn2.cache.amazonaws.com:6379",skip_full_coverage_check=True)

for index,value in enumerate(string.ascii_lowercase):
    rc.set(value,index)