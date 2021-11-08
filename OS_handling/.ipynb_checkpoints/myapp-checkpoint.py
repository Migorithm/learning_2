import os
import subprocess
my_env = os.environ.copy()
my_env["PATH"] = os.pathsep.join(["/opt/myapp/",my_env["PATH"]])
#'/opt/myapp/:/Users/we/google_course/venv/bin:/usr/local/bin:/usr/local/sbin:/opt/local/bin:/opt/local/sbin:/Library/Frameworks/Python.framework/Versions/3.10/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin:/opt/X11/bin'
#This is nice way to put old path and new path together and run the child process with the given path
result = subprocess.run(["myapp"],env=my_env)