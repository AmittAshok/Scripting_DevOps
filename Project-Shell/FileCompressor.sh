#!/bin/bash
#$Revision:001$
#$/Fri Jan 24 11:44:09 PM IST 2025$

# Variables
BASE=/home/amitt-ashok/Downloads
DAYS=10
DEPTH=1
RUN=0

#Check if given dir present or not
if [ ! -d $BASE ];
then
	echo "Directory not Present: $(basename "$BASE")"
	exit 1
fi
# Create Archive folder if not present
if [ ! -d $BASE/archive ];
then
	mkdir $BASE/archive
fi

# Find the file which are larger than 20 MB
for i in $(find $BASE -maxdepth $DEPTH -type f -size +500k);
do
	if [ $RUN -eq 0 ];
	then
		echo "[$(date "+%d/%m/%Y %H:%M:%S")] archiving $i ==> $BASE/archive"
		gzip $i || exit 1
		mv $i.gz $BASE/archive || exit 1
	fi
done

#Find file which are 10 days old
for in $(find $BASE -type f -mtime -20 | rm -rf   );
do
	echo "file older than 20days are deleted..."
done

