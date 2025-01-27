#!/bin/bash
#
echo "Enter D for Date.."
echo "Enter L for List of files.."
echo "Enter C for current directory location.."

read choice
case $choice in
	D)
		echo "Today date is:"
		date
		echo "ending"
		;;
	L)ls;;
	C)pwd;;
	*)echo "enter valid input.."
esac
