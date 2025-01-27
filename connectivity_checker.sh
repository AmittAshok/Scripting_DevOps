#!/bin/bash

set -x   # -x use for debug mode in script
read -p "Enther the site name which you to check:" site

ping -c 1 $site &> /dev/null    # &> /dev/null is use to divert output to the empty location

if [[ $? -eq 0 ]]
then
	echo "Connected successfully to $site"
else
	echo "Connection abort"
fi
