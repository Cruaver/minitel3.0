#!/usr/bin/python3
# -*-coding:utf-8 -* 
import os
import subprocess
import psutil
import signal
import pwd
import time
import sys
import fcntl
from getch import getch, pause


def get_pname(id):#{
    p = subprocess.Popen(["ps -o comm= {}".format(id)], stdout=subprocess.PIPE, shell=True)
    return str(p.communicate()[0])
        #}

def refresh(pid):
    while True:
        stats = {}
        stats['pid'] = psutil.Process(pid)
        stats['Cpu'] = stats['pid'].cpu_percent(interval = 1)
        stats['Memories'] = round(stats['pid'].memory_percent(), 1)
        stats['parentId'] = psutil.Process(pid).ppid()
        stats['Username'] = stats['pid'].username()
        stats['Cmdline'] = get_pname(pid).rstrip('\n')
        stats['Status'] = stats['pid'].status()
        return stats
    
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
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    dirs = os.listdir("/proc")
    for pid in dirs:#{
    	try:#{
            pidDel = input("PID du processus à Kill : ")
            if psutil.pid_exists(pidDel):#{
        	try:#{
        	    name = get_pname(pidDel)
        	    p = psutil.Process(pidDel)
        	    p.terminate()
        	    print "Vous avez kill le processus :", name.rstrip('\n')
        	    break
                #}
               	except psutil.AccessDenied:
        	    print "Vous n'avez pas les droits pour kill le processus", name.rstrip('\n')
            #}
            else:
        	print "Aucun processus avec le pid \"{}\" en cours.".format(pidDel)
        except (NameError, TypeError):
            print "Vous n'avez pas entrer un nombre entier."
        #}
    #}
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}

def statuts_process():#{
    os.system('setterm -term linux -back blue -fore white')
    os.system('clear')
    try:#{
        pidStat = input("PID du processus pour voir plus de détails : ")
        os.system('clear')
        if psutil.pid_exists(pidStat):#{
            fl = fcntl.fcntl(sys.stdin.fileno(), fcntl.F_GETFL)
            fcntl.fcntl(sys.stdin.fileno(), fcntl.F_SETFL, fl | os.O_NONBLOCK)
            realtime = 0
            while 42:
                try:#{
                    stats = refresh(pidStat)
                    print "PPID :", stats['parentId']
                    print "PID :", (pidStat)
                    print "Username :", stats['Username']
                    try:
                        print "Cmd name :", stats['Cmdline']
                        print "Statut :", stats['Status']
                        print "CPU usage :", stats['Cpu'], "%"
                        print "Memory usage :", stats['Memories'], "%"
                        time.sleep(1.5)
                        try:#{
                            realtime = sys.stdin.read()
                            if "\n" in realtime or "\r" in realtime:
                                break
                        #}
                        except IOError:
                            pass
                        time.sleep(1)
                        print "teste"
                        os.system('clear')
                #}
                    except psutil.AccessDenied:
                        print "Vous n'avez pas les droits sur ce processus pour voir plus de détails"
                except psutil.NoSuchProcess:
                    print "Le processus a ete ferme"
                    break
            #}
        else:
            print "Aucun processus avec le PID \"{}\" en cours.".format(pidStat)
    #}
    except (NameError, TypeError):
        print "Vous n'avez pas entrer un nombre entier."
        os.system('setterm -term linux -back black -fore white')
        return (0)
#}
