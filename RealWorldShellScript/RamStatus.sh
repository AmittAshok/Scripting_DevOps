#!/bin/bash

# Cheking RAM staus of the system
FREE_SPACE=$( free -mt | grep "Total"| awk '{print $4}')
threshold=8000
TO="amittashok24@gmail.com"
if [ $FREE_SPACE -le $threshold  ];
then
	echo "Warrning, RAM is running low..." | mail -s "RAM AlERT,Check System" $TO
else
	echo "RAM is sufficient:" $FREE_SPACE
fi

