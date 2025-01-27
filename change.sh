#!/bin/bash
#
files="/home/amitt-ashok/shell_script"

cd $files
for file in $files/*
do
	perms=$(stat -c '%A' "$file" )
	if [ "$perms" == "-rwxrw-r--" ];
	then
		chmod 640 $file
		
	else
		echo "Successfuly completed"
	fi
done
