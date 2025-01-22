#!/bin/bash
#
#Array is use to save number of variable or multiple values
#In array values are stored space separted
myArray=( 1 2 Hello 40.5 "AmittAshok" )
echo "All the values of the array... ${myArray[*]}"

echo "Number First: ${myArray[0]}"

# Print each value in separte line
for value in "${myArray[@]}";
do
	echo "$value"
done

#Find numbers value in arrya
#
echo "The length of arrya is: ${#myArray[*]}"
#Update values in arrya
myArray+=( Rama 4 5 )

echo "Updated value in array ${myArray[*]}"
