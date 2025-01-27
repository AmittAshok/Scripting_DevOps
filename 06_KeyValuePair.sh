#!/bin/bash
#
# How to store key-value in array and there retreival option
#
 declare -A myArray
 myArray=( [name]=Amitt [age]=34 [city]=Pune )
 echo " My name is ${myArray[name]} and my age is ${myArray[age]}"
