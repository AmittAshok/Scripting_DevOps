#!/bin/bash

# Checking free disk space of system
#
 free_disk=$(df -h | grep "sda2" | awk '{print $5}' | tr -d %)
 threshold=50

 if [ $free_disk -ge $threshold ];
 then
	 echo "Alert,Storage shriking..."
 else
	 echo "Sfficient storage in system:" $free_disk%
 fi

