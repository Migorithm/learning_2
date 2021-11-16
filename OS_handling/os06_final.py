#!/usr/bin/env python3
import sys
import csv
import re
import os


def error_counter(filename):
    error={}
    per_user={}
    with open(filename) as f:
        regex =r"(ERROR|INFO)([\w ']*)(?:\[?#?[0-9]*\])? ?\(([\.a-zA-Z]*)\)"
        for i in f.readlines():
            a= re.search(regex,i)
            if a:
                per_user[a.group(3)]=per_user.get(a.group(3),[0,0])

              #  print(a.group(1),a.group(2),a.group(3))
                if a.group(1)=="ERROR":
                    per_user[a.group(3)][1] +=1
                    if a.group(2) not in error:
                        error[a.group(2)] =1
                    else:
                        error[a.group(2)] +=1

                else:
                    per_user[a.group(3)][0] +=1



        error = sorted(error.items(),key=lambda x:x[1],reverse=True)
        per_user = sorted(per_user.items())
        lst=[]
        for i ,j in per_user:
            lst2=[]
            lst2.append(i)
            lst2.append(j[0])
            lst2.append(j[1])
            lst.append(tuple(lst2))
        f.close()
    error.insert(0,("Error","Count"))
    lst.insert(0,("Username","INFO","ERROR"))
    return error,lst

import time
def write_things():
    error, lst=error_counter(sys.argv[1])
    with open("error_message.csv","w") as e:
        writer=csv.writer(e)
        for i in error:
            writer.writerow(i)
        e.close()

    with open("user_statistics.csv","w") as u:
        writer2=csv.writer(u)
        for k in lst:
            writer2.writerow(k)
        u.close()
        
write_things()

