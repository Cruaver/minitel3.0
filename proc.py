#!/usr/bin/python3
# -*-coding:utf-8 -* 
import os
import subprocess
import psutil
import signal
import pwd

def get_pname(id):#{
    p = subprocess.Popen(["ps -o comm= {}".format(id)], stdout=subprocess.PIPE, shell=True)
    return str(p.communicate()[0])
#}

def get_process():#{
    tab = []
    dict = {}
    dirs = os.listdir("/proc")
    for pid in dirs:#{
        if pid.isdigit():#{
            name = get_pname(pid)
            dict["pid"] = pid.strip()
            dict["name"] = name.strip()
            tab.append(dict)
            dict = {}
        #}
    #}
    return (tab)
#}

def kill_process():#{
    dirs = os.listdir("/proc")
    for pid in dirs:#{
        pidDel = input("entrer le pid du processus a kill")
        name = get_pname(pidDel)
        p = psutil.Process(pidDel)
        p.terminate()
        print "vous avez kill {}".format(name)
        break
    #}
    return (0)
#}

def statuts_process():#{
    pidStat = input("entrer le pid du processus a voir en details")
    pStat = psutil.Process(pidStat)
    parentId = psutil.Process(pidStat).ppid()
    print (parentId)
    print (pidStat)
    print get_pname(pidStat)
    print "cpu usage", (pStat.cpu_percent(interval=1))
    print "memories usage", round((pStat.memory_percent()), 1)
    return (0)
#}
