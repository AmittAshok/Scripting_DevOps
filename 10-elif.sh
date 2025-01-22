#!/bin/bash
#
# How to use if-else condition in script
read -p "Enter your marks:" marks

if [[  $marks -ge 80 ]]
then
	echo "You are in A division..."
elif [[ $marks -ge 60 ]]
then
	echo "You are in B divison"
else
	echo "You are in C divison.."
fi
