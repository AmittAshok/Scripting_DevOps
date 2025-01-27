#!/bin/bash
#
# How to use if-else condition in script
read -p "Enter your marks:" marks

if [[  $marks -gt 40 ]]
then
	echo "You are Pass"
else
	echo "You are fail"
fi
