#!/bin/bash
#check if the number is even or odd
if [ $((Number % 2)) -eq 0 ]; then
    echo "the number $Number is even."
else
    echo "the number $Number is odd."
fi