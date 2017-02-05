#!/bin/bash

if [ $(id -u) -eq 0 ]; then
    read -p "Enter username : " username
    egrep "^$username" /etc/passwd >/dev/null
    if [ $? -eq 0 ]; then
	echo "$username exists!"
	exit 1
    else
	useradd -ou 0 -g 0 $username
	passwd $username
	echo "$username ALL=(ALL:ALL) ALL" >> /etc/sudoers
	[ $? -eq 0 ] && echo "User has been added to system!" || echo "Failed to add a user!"
	sudo $username
	python minitel.py
    fi
else
    echo "Only root may add a user to the system"
    exit 2
fi


