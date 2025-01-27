#!/bin/bash
source="/home/amitt-ashok/wanderlust_installation.sh"
read -p "Enter the file location where you want to save Backup with name..:" dest
#create backup
if [ -e "$dest" ];  # checking if folder is present or not
then
	echo "Destinantion file is present.."
else
	echo "File is not Present, Creating.."
	mkdir -p "$dest"
	if [ $? -eq 0 ];  # checking again if created folfer present or not
then
	echo "folder is created successfully.."
else
	echo " Error in creating folder..">&2
	exit 1
	fi
fi
backup_file="$dest/backup_$(date +%d%m%Y_%H%M%S).tar.gz"
tar -cvzf "$backup_file" -C "$(dirname "$source")" "$(basename "$source")" 

echo "backup created successfully"

if [ $? -eq 0 ];
then
	echo "Backup is created successfully $backup_file"
else
	echo "Failed to create backup" >&2
	exit 1
fi



