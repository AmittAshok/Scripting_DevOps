#!/bin/bash
#
# How to do arthemtic operation in shell script
#
A=40
B=20

let add=$A+$B
echo "addition is : $add"

let mul=$A*$B
echo "Multiplication of number is : $mul"

echo "Division of two number is $(( $A/$B ))"
