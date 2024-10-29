#!/usr/bin/python

for s in range(1, 51):
    if (s % 3 == 0 and s % 5 == 0):
        print('FizzBuzz')
    elif (s % 3 == 0):
        print('fizz')
        
    elif (s % 5 == 0):
        print('buzz')
    else:
        print(s)