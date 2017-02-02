#!/usr/bin/python3.4
# -*-coding:utf-8 -*
import os

def version_os():#{
    fileOpen = open('/etc/issue', 'r')
    fileRead = fileOpen.readlines()
    for line in fileRead:
        print(line)
    fileOpen.close()
    return (0)
#}

def uptime():#{
    from datetime import timedelta
    with open('/proc/uptime', 'r') as f:#{
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
    #}
    print(uptime_string)
    return (0)
#}

def version_kernel():#{
    fileOpen = open('/proc/version')
    fileRead = fileOpen.read()
    print(fileRead)
    fileOpen.close()
    return (0)
#}

def infos_hardware(choos):#{
    if choos == "cpu":
        os.system('lscpu')
    elif choos == "memory":
        os.system('free | grep "Mem"')
    elif choos == "disk":
        os.system('df -h | grep "/dev/"')
    return (0)
#}
    
def limit_open_file():#{
    fileOpen = open('/proc/sys/fs/file-nr')
    fileRead = fileOpen.read()
    print(fileRead)
    fileOpen.close()
    return (0)
#}

def limit_open_proc():#{
    fileOpen = open('/proc/sys/kernel/pid_max')
    fileRead = fileOpen.read()
    print(fileRead)
    fileOpen.close()
    return (0)
#}

def installed_package():#{
    os.system("dpkg-query -f '${binary:Package}\n' -W")
    return (0)
#}
