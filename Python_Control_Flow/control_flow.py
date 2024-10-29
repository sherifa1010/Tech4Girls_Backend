#!/usr/bin/python

age = input("please enter your age:")

if age <18:
    print("you are a minor.")
elif 18 <= age <= 64:
    print("you are an aldult.")
else:
    print("you are a senior.")