#!/bin/bash
#compare the numbers
Num1=7
Num2=6

if [[ "$Num1" -gt "$Num2" ]];
then
    echo "$Num1 is greater than $Num2."
elif [[ "$Num1" -lt "$Num2" ]];
then
    echo "$Num1 is less than $Num2."
else
    echo "$Num1 is equal to $Num2."
fi

    