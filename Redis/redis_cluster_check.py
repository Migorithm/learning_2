#!/Users/we/google_course/venv/bin/python3
from rediscluster import RedisCluster

rc = RedisCluster.from_url("redis://upgrade-test50.kitlrm.clustercfg.apn2.cache.amazonaws.com:6379",skip_full_coverage_check=True)

for ip,info in rc.cluster_info().items():
    print("IP:{}\ncluster_state : {}\ncluster_slots_assigned : {}\ncluster_known_nodes : {}\ncluster_size".format(ip,
                                               info["cluster_state"],
                                               info['cluster_slots_assigned'],
                                               info['cluster_known_nodes']))
    print()
    print()