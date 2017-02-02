#!/usr/bin/python3.4
# -*-coding:utf-8 -*
import os

def version_os():#{
    fileOpen = open('/etc/issue', 'r')
    fileRead = fileOpen.readlines()
    for line in fileRead:
        print(line)
    fileOpen.close()
    fileOpen = open('/etc/issue', 'r')
    fileRead = fileOpen.readline()
    if fileRead == '\n':
        break
    print fileRead
    fileOpen.close()
#}

def uptime():#{
    from datetime import timedelta
    with open('/proc/uptime', 'r') as f:#{
        uptime_seconds = float(f.readline().split()[0])
        uptime_string = str(timedelta(seconds = uptime_seconds))
    #}
    print(uptime_string)
#}

def version_kernel():#{
    fileOpen = open('/proc/version')
    fileRead = fileOpen.read()
    print(fileRead)
    fileOpen.close()
#}

def infos_hardware():#{
    cpu = os.system('lscpu')
    memory = os.system('free | grep "Mem"')
    disk = os.sytem('df -h | grep "/dev/"')
#}
    
def limit_open_file():#{
    fileOpen = open('/proc/sys/fs/file-nr')
    fileRead = fileOpen.read()
    print(fileRead)
    fileOpen.close()
#}

def limit_open_proc():#{
    fileOpen = open('/proc/sys/kernel/pid_max')
    fileRead = fileOpen.read()
    print(fileRead)
    fileOpen.close()
#}

def installed_package():#{
    os.system("dpkg-query -f '${binary:Package}\n' -W")                                                                                                                             #}
