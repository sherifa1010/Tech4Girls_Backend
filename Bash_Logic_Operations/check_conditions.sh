#!/bin/bash
#checking condition operaters

if [[ "$Num1" -gt 10  && "$Num2" -gt 10 ]]; 
then
   echo "both numbers are greater than 10."
elif [[ "$Num1" -gt 10  || "$Num2" -gt 10 ]]; 
then
   echo "aleast one number is greater than 10."
else
   echo "neither number is greater than 10."
fi
