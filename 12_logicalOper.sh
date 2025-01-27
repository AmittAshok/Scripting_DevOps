#!/bin/bash

read -p "Enter you age...:" age
read -p "Enter your country name:" country

if [ $age -ge 18 ] && [ $country == "India" ];
then
	echo "You can vote now"
else
	echo "You are not eligible.."
fi
