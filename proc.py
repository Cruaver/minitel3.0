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
    if psutil.pid_exists(pidStat):#{
  	pStat = psutil.Process(pidStat)
  	parentId = psutil.Process(pidStat).ppid()
	print "PPID :", (parentId)
  	print "PID :", (pidStat)
        print "Username :", pStat.username()
  	try:#{
  	    print pStat.cwd()
  	    print "Cmd name :", get_pname(pidStat).rstrip('\n')
  	    print "Statut :", pStat.status()
  	    print "CPU usage :", (pStat.cpu_percent(interval=1)), "%"
  	    print "Memories usage :", round((pStat.memory_percent()), 1), "%"
        #}
  	except psutil.AccessDenied:
  	    print "Vous n'avez pas les droits sur ce processus pour voir plus de détails"
    else:
        print "Aucun processus avec le PID \"{}\" en cours.".format(pidStat)
    #}
    except (NameError, TypeError):
        print "Vous n'avez pas entrer un nombre entier."
    os.system('setterm -term linux -back black -fore white')
    return (0)
#}
