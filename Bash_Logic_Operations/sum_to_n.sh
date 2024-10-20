#!/bin/bash
#calculate the sum of numbers from 1 to n
n=$3
sum=0
for (( i=1; i<=n; i++ ));
do
    sum+$((sum + i))
done 
    echo "the sum of numbers from 1 to $n is: $sum"