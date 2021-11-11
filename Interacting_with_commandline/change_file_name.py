import sys
import subprocess
a= sys.argv[1]
with open(a) as f:
    for i in f.readlines():
        old_name=i.strip()
        new_name=old_name.replace("jane","jdoe")
        subprocess.run(["mv",old_name,new_name])