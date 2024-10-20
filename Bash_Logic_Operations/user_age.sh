#!/bin/bash
#ask for user age
#checking age category

read -p "please enter yur age: " 
if [[ "$age" -lt 18 ]];
then
    echo "you are minor."
elif [["$age" -ge 18 && "$age" -le 64 ]];
then
    echo "you are an adult."
else
    echo "you are senior."
fi