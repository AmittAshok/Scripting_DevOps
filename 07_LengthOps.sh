#!/bin/bash
#
# Some operation on string
#
 myVar="Hello Baby, How are You"
 lenghtVar=${#myVar}

 echo "The Lenght of variable is $lenghtVar"	
 echo "Uppercase values..... ${myVar^^}"
 echo "Lowercase values..... ${myVar,,}"
