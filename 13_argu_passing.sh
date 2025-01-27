#!/bin/bash

if [ $# -eq 0 ]
then
	echo "Pass atleas one argumet..."
	exit 1
fi

echo "First Arguments is $1"
echo "Second Argument is $2"

echo "All argument which is passed $@"
echo "Total number of argument $#"

# read argument with for loop

for filename in $@
do
	echo "List of Argument passed $filename"
done
