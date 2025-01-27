#!/bin/bash
#

read -p "Enter the username which you want to check:" username

if id "$username" &>/dev/null; then
	echo "$username is present"
else
	sudo useradd -m  $username
	echo "$username created successfully"
fi

