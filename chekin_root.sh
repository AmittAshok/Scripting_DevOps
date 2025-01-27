#!/bin/bash

# checking is user is root or not

if [[ $UID -eq 0 ]];
then
	echo "Root login"
else
	echo "Someone else is there"
fi
