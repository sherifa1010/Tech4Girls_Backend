#!/bin/bash
#positional argguments in Bash Scripting
#$0=script's name or first argument
#$1=second argument
#2=third argument
#echo"hello,$1,how are doing?"
#echo"the first argument or the name of the script is :$0"
#echo"the second argument is :$1"
#echo"the third argument is :$2"
#echo"the fouth argument is :$3"
#touch file3
#mkdir folder3

#mv "$1","$2"
#echo "$1 has been moved into $2'

#if [condition]





#if [condition]
#  then
# statement
# fi

#age=2

#if  [[ "$age" -gt 18 && "$age" -lt 1 ]]
#then
    #echo "Age is valid"
#else
    #echo "Age is invalid"
#fi

#echo "how old are you"?
#read age

#age=26

#if [["$age" -gt 18 && "$age" -lt -o -eq 30 ]]
#then 
   # echo "Age is valid"
#else
    #echo "Age is invalid"
#fi

#age=17

#if [["$1" -gt 10 && "$1" -gt 10]]
#then 
#echo


#string="hi,ladies!"

#if [[! $string == "goodbye!"]]; then
    # echo "string is not equal to goodbye"
#else
   # echo 'string

#echo "Your Position:"
#read string

#if [[ $string == "admin" ]];
#then
#    echo "access granted"
#else
#    echo "access denied"
#fi
  
#while [condition]
#do
# [command]
# [command]
# [command]


 #number=2

 #while [ $number -le 10 ]
 #do
 #   echo "$number"
 #   number=$((number+1))
#done


#while true; do
#  echo "Enter a number or type 'q' to quit"
#  read number

 # if [[ "$number" == "q" ]]; then
 #  break
 # fi

  #echo "you entered $number"
#done

#echo "Exiting the loop"

if [ "$#" -ne 2 ]; then
    echo "usage: $0 <first name> <last name>"
    exit 1
fi
# Assign positional arguments to  variables
FIRST_NAME=$1
LAST_NAME=$2

#Display the greeting message
echo "Hello, $FIRST_NAME $LAST_NAME! welcome to 
Bash scripting."




